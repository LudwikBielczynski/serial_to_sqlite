// SimpleRx - the slave or the receiver
// based on https://forum.arduino.cc/index.php?topic=421081
#include <Arduino.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#include <printf.h>

#define CE_PIN 8
#define CSN_PIN 9

const byte SLAVE_ADDRESS[5] = {'R','x','0','0','1'};

RF24 radio(CE_PIN, CSN_PIN);

void setup() {
  bool isSetupSuccess = false;

  Serial.begin(9600);
  printf_begin();
  Serial.println("Powered up the microprocessor...");

  isSetupSuccess = radio.begin();
  // Serial.print("Receiver initialization status: ");
  Serial.println(isSetupSuccess);
  // radio.printDetails();v
  Serial.println();

  if (isSetupSuccess) {
    // Set the pipe on the selected address address
    radio.openReadingPipe(1, SLAVE_ADDRESS);
    radio.setDataRate(RF24_250KBPS);
    radio.setPALevel(RF24_PA_MIN);
    radio.printDetails();

    // Set module as a receiver
    radio.startListening();
    Serial.println("Ready to receive. Listening...");
  }
  else
    Serial.println("There were issues during initial setup. The receiver is not ready.");
}


bool getData(char * dataReceived, unsigned short dataReceivedSize) {
  bool hasNewData = false;
  if (radio.available()) {
    radio.read(dataReceived, dataReceivedSize);
    hasNewData = true;
  }
  return hasNewData;
}


void showData(bool hasNewData, char * dataReceived) {
  if (hasNewData == true) {
    Serial.print("Rx=");
    Serial.println(dataReceived);
    hasNewData = false;
  }
}


void loop() {
  unsigned short dataReceivedSize = 12;
  char dataReceived[dataReceivedSize];
  bool hasNewData = false;

  hasNewData = getData(dataReceived, dataReceivedSize);
  showData(hasNewData, dataReceived);
}
