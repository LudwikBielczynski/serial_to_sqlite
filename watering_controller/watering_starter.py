import json
import time
from typing import Dict

import pandas as pd
import RPi.GPIO as GPIO

from common.shares import LOCAL_DATABASES_PATH, RELAYS_CONFIG_PATH, RELAY_CHANNEL_PIN_BCM_MAP
from repositories.database import WateringSchedule
from repositories.database.sqlite import DatabaseSqlite

SLEEP_TIME_BETWEEN_CHECKS = 5 # s

if __name__ == '__main__':
    LOCAL_DATABASES_PATH.mkdir(parents=True, exist_ok=True)

    # Channel-section name mapping is stored locally in a config
    with open(RELAYS_CONFIG_PATH, 'r') as json_data:
        relays_config_json = json.load(json_data)

    channel_section_name_map = {
        channel_info['channel_nr']: channel_info['section_name']
        for channel_info in relays_config_json
        }

    # Set up relay and follow its state
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    channels_state = {} # type: Dict[int, str]
    for channel, pin in RELAY_CHANNEL_PIN_BCM_MAP.items():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        channels_state[channel] = GPIO.HIGH

    # Create database and initialize objects to handle operations on tables
    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'watering_schedule.db')
    watering_schedule = WateringSchedule(database_sqlite)

    while True:
        # Check tasks that should be triggered now
        should_water = watering_schedule.check_should_water(pd.Timestamp.utcnow())

        # keep or change state on the section


        time.sleep(SLEEP_TIME_BETWEEN_CHECKS)
