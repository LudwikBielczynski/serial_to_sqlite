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
const unsigned long SLEEP_INTERVAL_MS = 1;

void Microcontroller::sleep() {
  Serial.println("Starting to sleep");
  delay(1000);

  sleep_enable();
  set_sleep_mode(SLEEP_MODE_PWR_SAVE); // Power-save mode disables BOD p.34

  // CLKPR = 0x02;
  clock_prescale_set(clock_div_128);
  // sleep_cpu();

  delay(100);
  clock_prescale_set(clock_div_1);
  power_all_enable();
  sleep_disable();
  Serial.println("Woke up");

  delay(1000);
}