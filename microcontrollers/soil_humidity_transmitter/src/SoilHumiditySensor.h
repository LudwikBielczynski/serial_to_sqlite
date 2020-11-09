#include <Arduino.h>

#ifndef SOILHUMIDITYSENSOR_H
#define SOILHUMIDITYSENSOR_H

class SoilHumiditySensor{
  public:
    const uint8_t power_pin, sensor_pin;

    SoilHumiditySensor(uint8_t _power_pin, uint8_t _sensor_pin):
      power_pin{_power_pin},
      sensor_pin{_sensor_pin}
    {
      Serial.println("Initialized soil humidity sensor");
    };


    // functions used to return the value of the soil humidity from the sensor
    uint16_t measure(uint16_t soilHumiditySensorValue, float batteryVoltage);

  private:
    const float _voltageOutputMax = 3.0;

    // To stabilize the analogue PIN read-out
    void discardFewFirstAnalogueReads();

    // Function used to turn on the soil humidity sensor
    void turnOn();

    // Function used to prepare everything and turn off soil humidity sensor
    void turnOff();

};

#endif
