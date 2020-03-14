// the soil humidity sensor and the transmitter
// SimpleTx -
// based on https://forum.arduino.cc/index.php?topic=421081

#include <Arduino.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#include <printf.h>
#include <stdlib.h>
#include <string.h>

#define SENSOR_PIN A0
#define CE_PIN 8
#define CSN_PIN 9

RF24 radio(CE_PIN, CSN_PIN);
const byte SLAVE_ADDRESS[5] = {'R','x','A','A','A'};

// Transmitter general settings
const char * TRANSMITTER_NAME = "Tx1";
const unsigned long TRANSMITTER_SEND_INTERVAL_MS = 1000;
unsigned long previousTimeMs;

void setup() {
  bool isSetupSuccess = false;

  Serial.begin(9600);
  printf_begin();

  Serial.println("Starting the transmitter...");
  isSetupSuccess = radio.begin();
  // Serial.print("radio.begin() success: ");
  // Serial.println(isSetupSuccess);
  // radio.printDetails();

  if (isSetupSuccess) {
    // Set the pipe on the selected address address
    radio.openWritingPipe(SLAVE_ADDRESS);
    Serial.println("Pipe open");

    radio.setRetries(3, 5); // delay, count
    radio.setDataRate(RF24_250KBPS);
    radio.setPALevel(RF24_PA_MIN);

    // radio.printDetails();
    Serial.println("Ready to transmit...");
  }
  else
    Serial.println("There were issues during initial setup and the transmitter is not ready");
}


void prepareDataToSend(char * dataToSend, unsigned short soilHumiditySensorValue){
  strcat(dataToSend, TRANSMITTER_NAME);
  strcat(dataToSend, ";");

  // Cast soil humidity sensor from int to char and concat to the message
  char soilHumiditySensorValueStr[3] = "";
  itoa(soilHumiditySensorValue, soilHumiditySensorValueStr, 10);
  strcat(dataToSend, soilHumiditySensorValueStr);
}


bool send(char * dataToSend, unsigned short dataToSendSize) {
  bool isWriteSuccess = radio.write( dataToSend, dataToSendSize);

  Serial.print("Message to send: ");
  Serial.print(dataToSend);

  if (isWriteSuccess) {
    Serial.println(" | Transmission succeeded");
  }
  else {
    Serial.println(" | Transmission failed");
  }
  return isWriteSuccess;
}


void loop() {
  unsigned short dataToSendSize = 8;
  // char dataToSend[dataToSendSize] = "Tx1_000";
  unsigned long currentTimeMs = millis();
  if (currentTimeMs - previousTimeMs >= TRANSMITTER_SEND_INTERVAL_MS) {
    char dataToSend[dataToSendSize] = ""; // Important to zero this variable before preparing data

    // Read values from the humidity sensor
    int soilHumiditySensorValue = analogRead(SENSOR_PIN);
    prepareDataToSend(dataToSend, soilHumiditySensorValue);
    // Normalize humidity data to the calibrated values
    // outputValue = map(outputValue, 550, 0, 0, 100);

    // Send to the receiver
    send(dataToSend, dataToSendSize);
    previousTimeMs = millis();
  }
}
