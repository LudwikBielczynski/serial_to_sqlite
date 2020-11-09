#include "Microcontroller.h"

void Microcontroller::discardFewFirstAnalogueReads(){
  for (size_t i = 0; i < 10; i++)
  {
    analogRead(voltage_splitter_pin);
    delay(10);
  }
}

/****************************************************************************/

float Microcontroller::measureBatteryVoltage(unsigned short int averaged_measurements_nr) {
  analogReference(INTERNAL);

  discardFewFirstAnalogueReads();

  int voltagesSum = 0;

  for (size_t i = 0; i < averaged_measurements_nr; i++)
  {
    voltagesSum += analogRead(voltage_splitter_pin);
    delay(10);
  }
  float voltage = voltage_split_factor * reference_voltage * voltagesSum / (1024.0 * averaged_measurements_nr) + voltage_correction;

  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.println("V");
  return voltage;
}

/****************************************************************************/

const unsigned long SLEEP_INTERVAL_MS = 1;

void Microcontroller::sleep() {
  Serial.println("Starting to sleep");
  digitalWrite(microcontroller_led_on_pin, LOW);
  // delay(1000);

  sleep_enable();
  set_sleep_mode(SLEEP_MODE_PWR_SAVE); // Power-save mode disables BOD p.34

  clock_prescale_set(clock_div_128);
  // sleep_cpu();

  delay(50);
  // delay(10);
  clock_prescale_set(clock_div_1);
  power_all_enable();
  sleep_disable();

  Serial.println("Woke up");
  digitalWrite(microcontroller_led_on_pin, HIGH);
  delay(1000);
}