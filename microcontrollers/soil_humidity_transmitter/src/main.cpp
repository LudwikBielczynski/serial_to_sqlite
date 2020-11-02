// the soil humidity sensor and the transmitter
// SimpleTx -
// based on https://forum.arduino.cc/index.php?topic=421081

#include "Transmitter.h"
#include "SoilHumiditySensor.h"
#include "Microcontroller.h"
#include <printf.h>

// Pin layout
const uint8_t MICROCONTROLLER_ON_PIN = 7;
const uint8_t RADIO_POWER_PIN = 4;
const uint8_t SOIL_HUMIDITY_POWER_PIN = 5;
const uint8_t CE_PIN = 8;
const uint8_t CSN_PIN = 9;
const uint8_t SCK_PIN = 13; // default SCK pin
const uint8_t SOIL_HUMIDITY_SENSOR_PIN = 14; // A0
const uint8_t VOLTAGE_SPLITTER_PIN = 16; // A2

const uint64_t SLAVE_ADDRESS = 0xE6E6E6E6E6E6;

// Soil humidity settings
const unsigned short int SOIL_MOISTURE_MEASUREMENTS_NR = 1;
const unsigned short dataToSendSize = 12;
int soilHumiditySensorValue;

// Measure voltage settings
const unsigned short int VOLTAGE_MEASUREMENTS_NR = 10;
const float REFERENCE_VOLTAGE = 2.99;
const float VOLTAGE_SPLIT_FACTOR = 11.0; // based on (R1 + R2)/R2 where R1=100kOhm and R2=10kOhm
const float VOLTAGE_CORRECTION = 0.00;
float voltage;

// Transmitter transmitter(CE_PIN, CSN_PIN, SCK_PIN, RADIO_POWER_PIN, SLAVE_ADDRESS);
// SoilHumiditySensor soil_humidity_sensor(SOIL_HUMIDITY_POWER_PIN, SOIL_HUMIDITY_SENSOR_PIN);
// Microcontroller microcontroller(VOLTAGE_SPLITTER_PIN, VOLTAGE_SPLIT_FACTOR, REFERENCE_VOLTAGE, VOLTAGE_CORRECTION);

void setup() {
  Serial.begin(9600);
  Serial.println("Powered up the microprocessor...");
  pinMode(MICROCONTROLLER_ON_PIN, OUTPUT);
  digitalWrite(MICROCONTROLLER_ON_PIN, HIGH);

  // analogReference(EXTERNAL);
  // analogRead(VOLTAGE_SPLITTER_PIN); // First read after switching to external reference are not reliable
  // analogRead(SOIL_HUMIDITY_SENSOR_PIN);

  // printf_begin();
  pinMode(RADIO_POWER_PIN, OUTPUT);
  pinMode(SOIL_HUMIDITY_POWER_PIN, OUTPUT);
}

/****************************************************************************/

void loop() {
  Serial.println("Something");
  Serial.println(F_CPU);

  // Read battery voltage before other components are powered up
  // voltage = microcontroller.measureBatteryVoltage(VOLTAGE_MEASUREMENTS_NR);
  // Serial.println(voltage);
  delay(2000);

  // char dataToSend[dataToSendSize] = ""; // Important to zero this variable before preparing data

  // // // Measure soil moisture

  digitalWrite(SOIL_HUMIDITY_POWER_PIN, HIGH);
  Serial.println("SOIL_HUMIDITY_POWER_PIN");
  delay(2000);
  digitalWrite(SOIL_HUMIDITY_POWER_PIN, LOW);

  digitalWrite(RADIO_POWER_PIN, HIGH);
  Serial.println("RADIO_POWER_PIN");
  delay(2000);
  digitalWrite(RADIO_POWER_PIN, LOW);


  // soilHumiditySensorValue = soil_humidity_sensor.measure();
  // Serial.println(soilHumiditySensorValue);
  // // Send data to the receiver
  // digitalWrite(RADIO_POWER_PIN, HIGH);
  // transmitter.turnOn();
  // transmitter.setUp();
  // transmitter.prepareDataToSend(dataToSend, soilHumiditySensorValue, voltage);
  // transmitter.sendData(dataToSend, dataToSendSize);
  // transmitter.turnOff();

  // microcontroller.sleep();

}
