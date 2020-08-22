from datetime import datetime
import logging
import os
from pathlib import Path
import sqlite3

from serial import Serial

from common.shares import LOCAL_DATABASES_PATH
from repositories.database import SoilHumidityTable, BatteryStateTable
from repositories.database.sqlite import DatabaseSqlite
from sensor_handler.decode_message import decode_message

if __name__ == '__main__':
    port = '/dev/ttyACM0'
    baud_rate = 9600

    LOCAL_DATABASES_PATH.mkdir(parents=True, exist_ok=True)

    # Create database and initialize objects to handle operations on tables
    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'sensors_data.db')
    soil_humidity_table = SoilHumidityTable(database_sqlite)
    battery_state_table = BatteryStateTable(database_sqlite)

    # Read from serial port constantly
    with Serial(port, baud_rate) as serial:
        while True:
            message = serial.readline() \
                            .decode('utf-8') \
                            .replace('\r', '') \
                            .replace('\n', '')
            if 'Rx' == message.split('=')[0]:
                transmitter_name, soil_humidity_value, battery_state = decode_message(message)

                # Prepare message
                now = datetime.now()
                soil_humidity_table.insert({'insert_datetime': now,
                                            'transmitter_name': transmitter_name,
                                            'sensor_value': soil_humidity_value,
                                           })
                battery_state_table.insert({'insert_datetime': now,
                                            'transmitter_name': transmitter_name,
                                            'sensor_value': battery_state,
                                           })
                # print(message)
