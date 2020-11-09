#include <Arduino.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#ifndef TRANSMITTER_H
#define TRANSMITTER_H

class Transmitter{
  public:
    const uint8_t ce_pin, csn_pin, sck_pin, power_pin;
    uint64_t slave_address;
    RF24 *radio;

    Transmitter(uint8_t _ce_pin,
                uint8_t _csn_pin,
                uint8_t _sck_pin,
                uint8_t _power_pin,
                uint64_t _slave_address):
      ce_pin{_ce_pin},
      csn_pin{_csn_pin},
      sck_pin{_sck_pin},
      power_pin{_power_pin},
      slave_address{_slave_address}
    {
      radio = new RF24(ce_pin, csn_pin);
    };

    // Function used to turn on the transmitter
    void turnOn();

    // Function used to set up the transmitter ready to transmit
    void setUp();

    // Function used to prepare data in a format valid to be send
    void prepareDataToSend(char * dataToSend, unsigned short soilHumiditySensorValue, float voltage);

    // Function used to send the prepared data to the receiver
    bool sendData(char * dataToSend, unsigned short dataToSendSize);

    // Function used to prepare everything and turn of the transmitter
    void turnOff();
};

#endif
