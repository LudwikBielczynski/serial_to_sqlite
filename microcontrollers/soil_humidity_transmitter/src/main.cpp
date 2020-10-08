// the soil humidity sensor and the transmitter
// SimpleTx -
// based on https://forum.arduino.cc/index.php?topic=421081

#include "Transmitter.h"
#include "SoilHumiditySensor.h"
#include "Microcontroller.h"
#include <printf.h>

// Pin layout
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
const float VOLTAGE_CORRECTION = 0.60;
float voltage;

Transmitter transmitter(CE_PIN, CSN_PIN, SCK_PIN, RADIO_POWER_PIN, SLAVE_ADDRESS);
SoilHumiditySensor soil_humidity_sensor(SOIL_HUMIDITY_POWER_PIN, SOIL_HUMIDITY_SENSOR_PIN);
Microcontroller microcontroller(VOLTAGE_SPLITTER_PIN, VOLTAGE_SPLIT_FACTOR, REFERENCE_VOLTAGE, VOLTAGE_CORRECTION);

void setup() {
  Serial.begin(9600);
  Serial.println("Powered up the microprocessor...");

  // analogReference(EXTERNAL);
  analogRead(VOLTAGE_SPLITTER_PIN); // First read after switching to external reference are not reliable
  analogRead(SOIL_HUMIDITY_SENSOR_PIN);

  printf_begin();
  pinMode(RADIO_POWER_PIN, OUTPUT);
  pinMode(SOIL_HUMIDITY_POWER_PIN, OUTPUT);
}

/****************************************************************************/

void loop() {

  // Read battery voltage before other components are powered up
  voltage = microcontroller.measureBatteryVoltage(VOLTAGE_MEASUREMENTS_NR);

  char dataToSend[dataToSendSize] = ""; // Important to zero this variable before preparing data

  // // Measure soil moisture
  soilHumiditySensorValue = soil_humidity_sensor.measure();

  // Send data to the receiver
  transmitter.turnOn();
  transmitter.setUp();
  transmitter.prepareDataToSend(dataToSend, soilHumiditySensorValue, voltage);
  transmitter.sendData(dataToSend, dataToSendSize);
  transmitter.turnOff();

  microcontroller.sleep();

}
