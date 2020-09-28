// the soil humidity sensor and the transmitter
// SimpleTx -
// based on https://forum.arduino.cc/index.php?topic=421081

#include <Arduino.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <printf.h>
#include <avr/sleep.h>
#include <avr/power.h>

// Pin layout
const uint8_t RADIO_POWER_PIN = 4;
const uint8_t SOIL_HUMIDITY_POWER_PIN = 5;
const uint8_t CE_PIN = 8;
const uint8_t CSN_PIN = 9;
const uint8_t SCK_PIN = 13; // default SCK pin
const uint8_t SENSOR_PIN = 14; // A0
const uint8_t VOLTAGE_SPLITTER_PIN = 16; // A2

// Transmitter settings
// RF24 radio(CE_PIN, CSN_PIN);

const byte SLAVE_ADDRESS[5] = {'R','x','0','0','1'};

const char * TRANSMITTER_NAME = "Tx1";
const unsigned long TRANSMITTER_SEND_INTERVAL_MS = 1000; // Once per 5sec
// const unsigned long long TRANSMITTER_SEND_INTERVAL_MS = 1800000; // Once per 30min
bool shouldStartWithMeasurement = true;
unsigned long long previousTimeMs;
unsigned long long currentTimeMs;
bool isLargerThanInterval = false;

// Soil humidity settings
const unsigned short int SOIL_MOISTURE_MEASUREMENTS_NR = 1;
const unsigned short dataToSendSize = 12;
int soilHumiditySensorValue;

// Measure voltage settings
const unsigned short int VOLTAGE_MEASUREMENTS_NR = 10;
const float REFERENCE_VOLTAGE = 2.99;
const float VOLTAGE_SPLIT_FACTOR = 11.0; // based on (R1 + R2)/R2 where R1=100kOhm and R2=10kOhm
const float VOLTAGE_CORRECTION = 0.60;
int voltagesSum = 0;
float voltage;

class Transmitter{
  public:
    const uint8_t ce_pin, csn_pin, sck_pin;
    RF24 *radio;

    Transmitter(uint8_t _ce_pin, uint8_t _csn_pin, uint8_t _sck_pin):
      ce_pin{_ce_pin},
      csn_pin{_csn_pin},
      sck_pin{_sck_pin}
    {
      Serial.println("Initialized transmitter...");
      radio = new RF24(ce_pin, csn_pin);
    };

    void setUp();

    bool sendData(char * dataToSend, unsigned short dataToSendSize);

    void turnOff();
};

void Transmitter::setUp() {
  Serial.println("Activate radio");
  digitalWrite(RADIO_POWER_PIN, HIGH);
  delay(200);

  Serial.println("Starting the transmitter...");
  radio = new RF24(ce_pin, csn_pin);

  pinMode(ce_pin, INPUT);
  pinMode(sck_pin, OUTPUT);

  bool isSetupSuccess = radio->begin();
  Serial.print("radio.begin() success: ");
  Serial.println(isSetupSuccess);

  // radio->powerUp();

  if (isSetupSuccess) {
    // radio.setAutoAck(false);

    // Set the pipe on the selected address address
    radio->openWritingPipe(SLAVE_ADDRESS);
    Serial.println("Pipe open");

    radio->setRetries(3, 5); // delay, count
    radio->setDataRate(RF24_250KBPS);
    radio->setPALevel(RF24_PA_MIN);

    Serial.println("Ready to transmit...");
  }
  else
    Serial.println("There were issues during initial setup and the transmitter is not ready");
    // radio->printDetails();
}

bool Transmitter::sendData(char * dataToSend, unsigned short dataToSendSize) {
  Serial.println("Trying to send data");
  bool isWriteSuccess = radio->write(dataToSend, dataToSendSize);

  Serial.print("Message to send: ");
  Serial.print(dataToSend);

  if (isWriteSuccess) {
    Serial.println(" | Transmission succeeded");
  }
  else {
    Serial.println(" | Transmission failed");
  }

  if (radio->failureDetected) {
    Serial.println("A failure was detected. Trying to Reset configuration");
    radio->failureDetected = 0; // Reset the detection value
    Transmitter::setUp();
  }
  else{
    Serial.println("Data sent");
  }

  return isWriteSuccess;
}

void Transmitter::turnOff() {
  // radio.powerDown();

  // Output pins to input so the current is not drawn
  pinMode(CE_PIN, INPUT);
  pinMode(sck_pin, INPUT);

  digitalWrite(RADIO_POWER_PIN, LOW); // Switch off the low side switch transistor

  Serial.println("Deactivated radio");

}

Transmitter transmitter(CE_PIN, CSN_PIN, SCK_PIN);

void setup() {
  Serial.begin(9600);
  Serial.println("Powered up the microprocessor...");

  // Transmitter transmitter(CE_PIN, CSN_PIN);

  analogReference(EXTERNAL);
  analogRead(VOLTAGE_SPLITTER_PIN); // First read after switching to external reference are not reliable
  analogRead(SENSOR_PIN);

  printf_begin();
  pinMode(RADIO_POWER_PIN, OUTPUT);
  pinMode(SOIL_HUMIDITY_POWER_PIN, OUTPUT);

  transmitter.setUp();
}

float measureBatteryVoltage() {
  voltagesSum = 0;
  for (size_t i = 0; i < VOLTAGE_MEASUREMENTS_NR; i++)
  {
    voltagesSum += analogRead(VOLTAGE_SPLITTER_PIN);
    delay(10);
  }
  // Serial.println(voltagesSum / VOLTAGE_MEASUREMENTS_NR);
  float voltage = VOLTAGE_SPLIT_FACTOR * REFERENCE_VOLTAGE * voltagesSum / (1024.0 * VOLTAGE_MEASUREMENTS_NR) + VOLTAGE_CORRECTION;
  // Serial.println(voltage);
  return voltage;
}


uint8_t measureSoilHumidity() {
    digitalWrite(SOIL_HUMIDITY_POWER_PIN, HIGH);
    delay(100);
    soilHumiditySensorValue = analogRead(SENSOR_PIN);
    // Serial.println(soilHumiditySensorValue);
    digitalWrite(SOIL_HUMIDITY_POWER_PIN, LOW); // Power sensor down

    return soilHumiditySensorValue;
}


void prepareDataToSend(char * dataToSend, unsigned short soilHumiditySensorValue, float voltage){
  strcat(dataToSend, TRANSMITTER_NAME);
  strcat(dataToSend, ";");

  // Cast soil humidity sensor from int to char and concat to the message
  char soilHumiditySensorValueStr[3] = "";
  itoa(soilHumiditySensorValue, soilHumiditySensorValueStr, 10);
  strcat(dataToSend, soilHumiditySensorValueStr);

  // Cat voltage
  strcat(dataToSend, ";");
  char voltageStr[4] = "";
  dtostrf(voltage, 3, 2, voltageStr);
  strcat(dataToSend, voltageStr);
}

void sleep_microcontroller() {
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

void loop() {
  currentTimeMs = millis();
  isLargerThanInterval = currentTimeMs - previousTimeMs >= TRANSMITTER_SEND_INTERVAL_MS;
  if (isLargerThanInterval | shouldStartWithMeasurement) {
    // Repeat few times the measurement to get the precision and sleep afterwards
    for (size_t i = 0; i < SOIL_MOISTURE_MEASUREMENTS_NR; i++)
    {
      // Read battery voltage before other components are powered up
      voltage = measureBatteryVoltage();

      char dataToSend[dataToSendSize] = ""; // Important to zero this variable before preparing data

      // // Measure soil moisture
      soilHumiditySensorValue = measureSoilHumidity();

      // Send data to the receiver
      prepareDataToSend(dataToSend, soilHumiditySensorValue, voltage);

      transmitter.setUp();
      transmitter.sendData(dataToSend, dataToSendSize);
      transmitter.turnOff();
    }
    sleep_microcontroller();

    shouldStartWithMeasurement = false;
    previousTimeMs = millis();
  }
}
