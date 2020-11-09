// the soil humidity sensor and the transmitter

#include "Transmitter.h"
#include "SoilHumiditySensor.h"
#include "Microcontroller.h"
#include <printf.h>

// Pin layout
const uint8_t MICROCONTROLLER_LED_ON_PIN = 7;
const uint8_t RADIO_POWER_PIN = 4;
const uint8_t SOIL_HUMIDITY_POWER_PIN = 5;
const uint8_t CE_PIN = 8;
const uint8_t CSN_PIN = 9;
const uint8_t SCK_PIN = 13; // default SCK pin
const uint8_t SOIL_HUMIDITY_SENSOR_PIN = 14; // A0
const uint8_t VOLTAGE_SPLITTER_PIN = 16; // A2

// Measure voltage settings
const unsigned short int VOLTAGE_MEASUREMENTS_NR = 10;
const float REFERENCE_VOLTAGE = 1.1;
const float VOLTAGE_SPLIT_FACTOR = 11.0; // based on (R1 + R2)/R2 where R1=100kOhm and R2=10kOhm
const float VOLTAGE_CORRECTION = 0.00;

// Soil humidity settings
const unsigned short int SOIL_MOISTURE_MEASUREMENTS_NR = 1;
int soilHumiditySensorValue;

// Transmitter settings
const uint64_t SLAVE_ADDRESS = 0xE6E6E6E6E6E6;
const unsigned short dataToSendSize = 12;

/****************************************************************************/

void setup() {
  Serial.begin(9600);
  Serial.println("Powered up the microprocessor...");
  pinMode(MICROCONTROLLER_LED_ON_PIN, OUTPUT);
  digitalWrite(MICROCONTROLLER_LED_ON_PIN, HIGH);

  // printf_begin();
  pinMode(RADIO_POWER_PIN, OUTPUT);
  pinMode(SOIL_HUMIDITY_POWER_PIN, OUTPUT);
}

/****************************************************************************/

void loop() {
  Serial.print("CPU frequency: ");
  Serial.println(F_CPU);
  delay(1000);

  // Read battery voltage before other components are powered up
  Microcontroller microcontroller(MICROCONTROLLER_LED_ON_PIN,
                                  VOLTAGE_SPLITTER_PIN,
                                  VOLTAGE_SPLIT_FACTOR,
                                  REFERENCE_VOLTAGE,
                                  VOLTAGE_CORRECTION);
  float voltage = 0;
  voltage = microcontroller.measureBatteryVoltage(VOLTAGE_MEASUREMENTS_NR);

  // Measure soil moisture
  SoilHumiditySensor soil_humidity_sensor(SOIL_HUMIDITY_POWER_PIN, SOIL_HUMIDITY_SENSOR_PIN);
  uint16_t soilHumiditySensorValue = 0;
  soilHumiditySensorValue = soil_humidity_sensor.measure(soilHumiditySensorValue, voltage);

  // Send data to the receiver
  Transmitter transmitter(CE_PIN, CSN_PIN, SCK_PIN, RADIO_POWER_PIN, SLAVE_ADDRESS);
  transmitter.turnOn();
  transmitter.setUp();

  char dataToSend[dataToSendSize] = ""; // Important to zero this variable before preparing data
  transmitter.prepareDataToSend(dataToSend, soilHumiditySensorValue, voltage);
  Serial.println(dataToSend);
  transmitter.sendData(dataToSend, dataToSendSize);

  transmitter.turnOff();

  microcontroller.sleep();

}
