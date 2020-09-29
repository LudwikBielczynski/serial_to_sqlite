#include "Transmitter.h"

const char * TRANSMITTER_NAME = "Tx1";

void Transmitter::turnOn() {
  // Function used to turn on the transmitter
  Serial.println("Activate radio");
  digitalWrite(power_pin, HIGH);
  delay(200);

  pinMode(ce_pin, INPUT);
  pinMode(sck_pin, OUTPUT);
}

/****************************************************************************/

void Transmitter::setUp() {
  // Function used to set up the transmitter ready to transmit
  Serial.println("Starting the transmitter...");
  radio = new RF24(ce_pin, csn_pin);

  bool isSetupSuccess = radio->begin();
  Serial.print("radio.begin() success: ");
  Serial.println(isSetupSuccess);

  // radio->powerUp();

  if (isSetupSuccess) {
    // radio.setAutoAck(false);

    // Set the pipe on the selected address address
    radio->openWritingPipe(slave_address);
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

/****************************************************************************/

void Transmitter::prepareDataToSend(char * dataToSend,
                                    unsigned short soilHumiditySensorValue,
                                    float voltage){
  // Function used to prepare data in a format valid to be send
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

/****************************************************************************/

bool Transmitter::sendData(char * dataToSend, unsigned short dataToSendSize) {
  // Function used to send the prepared data to the receiver
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

/****************************************************************************/

void Transmitter::turnOff() {
  // Function used to prepare everything and turn of the transmitter
  // radio.powerDown();

  // Output pins to input so the current is not drawn
  pinMode(ce_pin, INPUT);
  pinMode(sck_pin, INPUT);

  digitalWrite(power_pin, LOW); // Switch off the low side switch transistor

  Serial.println("Deactivated radio");

}
