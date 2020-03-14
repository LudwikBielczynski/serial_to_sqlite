import logging
import os
import sqlite3

from serial import Serial

from serial_to_sqlite.database import SoilHumidityTable, BatteryStateTable
from serial_to_sqlite.decode_message import decode_message
os.getcwd()

port = "/dev/ttyACM0"
baud_rate = 9600

# Create database and tables if needed
connection = sqlite3.connect('sensors_data.db')

soil_humidity_table = SoilHumidityTable(connection)
if not soil_humidity_table.exists():
    soil_humidity_table.create()

battery_state_table = BatteryStateTable(connection)
if not battery_state_table.exists():
    battery_state_table.create()


# Read from serial port constantly
with Serial(port, baud_rate) as serial:
    while True:
        message = serial.readline() \
                        .decode('utf-8') \
                        .replace('\r', '') \
                        .replace('\n', '')
        if 'Rx' == message.split('=')[0]:
            transmitter_name, soil_humidity_value, battery_state = decode_message(message)
            soil_humidity_table.insert(transmitter_name, soil_humidity_value)
            battery_state_table.insert(transmitter_name, battery_state)

connection.close()
