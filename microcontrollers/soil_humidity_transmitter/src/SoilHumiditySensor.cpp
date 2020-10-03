#include "SoilHumiditySensor.h"

void SoilHumiditySensor::turnOn() {
  // Function used to turn on the soil humidity sensor
  digitalWrite(power_pin, HIGH);
  delay(100);
}

/****************************************************************************/

void SoilHumiditySensor::turnOff() {
  // Function used to prepare everything and turn off soil humidity sensor
  digitalWrite(power_pin, LOW); // Power sensor down
}

uint8_t SoilHumiditySensor::measure() {
  // functions used to return the value of the soil humidity from the sensor
  SoilHumiditySensor::turnOn();

  // TODO: Implement several averaged reads
  int soilHumiditySensorValue;
  soilHumiditySensorValue = analogRead(sensor_pin);
  // Serial.println(soilHumiditySensorValue);

  SoilHumiditySensor::turnOff();

  return soilHumiditySensorValue;
}
