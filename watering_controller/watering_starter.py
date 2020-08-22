import time
from typing import Dict

import pandas as pd

from common.shares import LOCAL_DATABASES_PATH
from repositories.database import WateringSchedule
from repositories.database.sqlite import DatabaseSqlite

SLEEP_TIME_BETWEEN_CHECKS = 5 # s

if __name__ == '__main__':
    LOCAL_DATABASES_PATH.mkdir(parents=True, exist_ok=True)

    channels_state = {} # type: Dict[int, str]


    # Create database and initialize objects to handle operations on tables
    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'watering_schedule.db')
    watering_schedule = WateringSchedule(database_sqlite)

    while True:
        # Check tasks that should be triggered now
        watering_schedule.check_task(pd.Timestamp.utcnow())
        # Trigger on the relay a channel corresponding to the section


        time.sleep(SLEEP_TIME_BETWEEN_CHECKS)