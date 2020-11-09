#include "SoilHumiditySensor.h"

void SoilHumiditySensor::discardFewFirstAnalogueReads(){
  for (size_t i = 0; i < 10; i++)
  {
    analogRead(sensor_pin);
    delay(10);
  }
}

/****************************************************************************/

void SoilHumiditySensor::turnOn() {
  // Function used to turn on the soil humidity sensor
  digitalWrite(power_pin, HIGH);
  Serial.println("Turned on soil humidity sensor");
  delay(100);
}

/****************************************************************************/

void SoilHumiditySensor::turnOff() {
  // Function used to prepare everything and turn off soil humidity sensor
  digitalWrite(power_pin, LOW); // Power sensor down
  Serial.println("Turned off soil humidity sensor");
}

/****************************************************************************/

uint16_t SoilHumiditySensor::measure(uint16_t soilHumiditySensorValue,
                                     float batteryVoltage) {
  // Measured battery voltage will be used as the reference
  analogReference(DEFAULT);

  // functions used to return the value of the soil humidity from the sensor
  SoilHumiditySensor::turnOn();

  SoilHumiditySensor::discardFewFirstAnalogueReads();

  soilHumiditySensorValue = analogRead(sensor_pin);
  Serial.print("Soil humidity sensor value: ");
  Serial.print(soilHumiditySensorValue);
  Serial.print("; corrected: ");

  float voltageCorrection = batteryVoltage / _voltageOutputMax;
  Serial.print(soilHumiditySensorValue * voltageCorrection);
  Serial.print("; voltage correction: ");
  Serial.println(voltageCorrection);

  soilHumiditySensorValue = static_cast<int>(soilHumiditySensorValue * voltageCorrection);
  SoilHumiditySensor::turnOff();

  return soilHumiditySensorValue;
}
