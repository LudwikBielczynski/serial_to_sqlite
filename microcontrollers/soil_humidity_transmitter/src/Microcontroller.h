#include <Arduino.h>
#include <avr/sleep.h>
#include <avr/power.h>

#ifndef MICROCONTROLLER_H
#define MICROCONTROLLER_H

class Microcontroller{
  public:
    uint8_t voltage_splitter_pin;
    float voltage_split_factor, reference_voltage, voltage_correction;

    Microcontroller(uint8_t _voltage_splitter_pin,
                    float _voltage_split_factor,
                    float _reference_voltage,
                    float _voltage_correction):
      voltage_splitter_pin{_voltage_splitter_pin},
      voltage_split_factor{_voltage_split_factor},
      reference_voltage{_reference_voltage},
      voltage_correction{_voltage_correction}
    {
      Serial.println("Initialized microcontroller...");
    };

    // Functions used to measure battery voltage before the linear voltage regulator
    float measureBatteryVoltage(unsigned short int averaged_measurements_nr);

    // Function used to turn on sleep mode of ATmega
    void sleep();
};

#endif
