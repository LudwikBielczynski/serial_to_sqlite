// the soil humidity sensor and the transmitter
// SimpleTx -
// based on https://forum.arduino.cc/index.php?topic=421081

#include "Transmitter.h"
#include "SoilHumiditySensor.h"
#include <printf.h>
#include <avr/sleep.h>
#include <avr/power.h>

// Pin layout
const uint8_t RADIO_POWER_PIN = 4;
const uint8_t SOIL_HUMIDITY_POWER_PIN = 5;
const uint8_t CE_PIN = 8;
const uint8_t CSN_PIN = 9;
const uint8_t SCK_PIN = 13; // default SCK pin
const uint8_t SOIL_HUMIDITY_SENSOR_PIN = 14; // A0
const uint8_t VOLTAGE_SPLITTER_PIN = 16; // A2

// Transmitter settings
// RF24 radio(CE_PIN, CSN_PIN);

const uint64_t SLAVE_ADDRESS = 0xE6E6E6E6E6E6;

const unsigned long TRANSMITTER_SEND_INTERVAL_MS = 1000; // Once per 5sec
// const unsigned long long TRANSMITTER_SEND_INTERVAL_MS = 1800000; // Once per 30min
bool shouldStartWithMeasurement = true;
unsigned long long previousTimeMs;
unsigned long long currentTimeMs;
bool isLargerThanInterval = false;

// Soil humidity settings
const unsigned short int SOIL_MOISTURE_MEASUREMENTS_NR = 1;
const unsigned short dataToSendSize = 12;
int soilHumiditySensorValue;

// Measure voltage settings
const unsigned short int VOLTAGE_MEASUREMENTS_NR = 10;
const float REFERENCE_VOLTAGE = 2.99;
const float VOLTAGE_SPLIT_FACTOR = 11.0; // based on (R1 + R2)/R2 where R1=100kOhm and R2=10kOhm
const float VOLTAGE_CORRECTION = 0.60;
int voltagesSum = 0;
float voltage;

Transmitter transmitter(CE_PIN, CSN_PIN, SCK_PIN, RADIO_POWER_PIN, SLAVE_ADDRESS);
SoilHumiditySensor soil_humidity_sensor(SOIL_HUMIDITY_POWER_PIN, SOIL_HUMIDITY_SENSOR_PIN);

void setup() {
  Serial.begin(9600);
  Serial.println("Powered up the microprocessor...");

  analogReference(EXTERNAL);
  analogRead(VOLTAGE_SPLITTER_PIN); // First read after switching to external reference are not reliable
  analogRead(SOIL_HUMIDITY_SENSOR_PIN);

  printf_begin();
  pinMode(RADIO_POWER_PIN, OUTPUT);
  pinMode(SOIL_HUMIDITY_POWER_PIN, OUTPUT);

  transmitter.setUp();
}

/****************************************************************************/

float measureBatteryVoltage() {
  voltagesSum = 0;
  for (size_t i = 0; i < VOLTAGE_MEASUREMENTS_NR; i++)
  {
    voltagesSum += analogRead(VOLTAGE_SPLITTER_PIN);
    delay(10);
  }
  // Serial.println(voltagesSum / VOLTAGE_MEASUREMENTS_NR);
  float voltage = VOLTAGE_SPLIT_FACTOR * REFERENCE_VOLTAGE * voltagesSum / (1024.0 * VOLTAGE_MEASUREMENTS_NR) + VOLTAGE_CORRECTION;
  // Serial.println(voltage);
  return voltage;
}

/****************************************************************************/

void sleep_microcontroller() {
    Serial.println("Starting to sleep");

    delay(1000);
    // digitalWrite(SCK_PIN, LOW);

    // set_sleep_mode(SLEEP_MODE_PWR_SAVE);
    // set_sleep_mode(SLEEP_MODE_PWR_DOWN);
    // sleep_enable();
    // sleep_mode();
    // clock_prescale_set(clock_div_4);
    // // CLKPR = 0x02;
    // delay(3000);
    // clock_prescale_set(clock_div_1);
    // power_all_enable();
    // sleep_disable();
    Serial.println("Woke up");
}

/****************************************************************************/

void loop() {
  currentTimeMs = millis();
  isLargerThanInterval = currentTimeMs - previousTimeMs >= TRANSMITTER_SEND_INTERVAL_MS;
  if (isLargerThanInterval | shouldStartWithMeasurement) {
    // Repeat few times the measurement to get the precision and sleep afterwards
    for (size_t i = 0; i < SOIL_MOISTURE_MEASUREMENTS_NR; i++)
    {
      // Read battery voltage before other components are powered up
      voltage = measureBatteryVoltage();

      char dataToSend[dataToSendSize] = ""; // Important to zero this variable before preparing data

      // // Measure soil moisture
      soilHumiditySensorValue = soil_humidity_sensor.measure();

      // Send data to the receiver
      transmitter.turnOn();
      transmitter.setUp();
      transmitter.prepareDataToSend(dataToSend, soilHumiditySensorValue, voltage);
      transmitter.sendData(dataToSend, dataToSendSize);
      transmitter.turnOff();
    }
    sleep_microcontroller();

    shouldStartWithMeasurement = false;
    previousTimeMs = millis();
  }
}
