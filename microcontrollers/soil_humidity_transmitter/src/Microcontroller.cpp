#include "Microcontroller.h"

float Microcontroller::measureBatteryVoltage(unsigned short int averaged_measurements_nr) {
  int voltagesSum = 0;

  for (size_t i = 0; i < averaged_measurements_nr; i++)
  {
    voltagesSum += analogRead(voltage_splitter_pin);
    delay(10);
  }
  // Serial.println(voltagesSum / VOLTAGE_MEASUREMENTS_NR);
  float voltage = voltage_split_factor * reference_voltage * voltagesSum / (1024.0 * averaged_measurements_nr) + voltage_correction;
  // Serial.println(voltage);
  return voltage;
}

/****************************************************************************/

void Microcontroller::sleep() {
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