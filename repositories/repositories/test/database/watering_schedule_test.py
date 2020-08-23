from datetime import datetime, time

import pandas as pd

from repositories.database import  WateringSchedule
from repositories.database.sqlite import DatabaseSqlite

COMMUNICATION_DB_NAME_TEST = 'test.db'

def test_schedule_watering(tmp_path):
    # Arange
    path = tmp_path

    database_sqlite = DatabaseSqlite(tmp_path, COMMUNICATION_DB_NAME_TEST)
    watering_schedule = WateringSchedule(database_sqlite)

    scheduled_watering = {'insert_datetime_utc': datetime.utcnow(),
                          'channel': 1,
                          'start_time_utc': '10:00',
                          'end_time_utc': '20:00',
                          'weekday': 1,
                         }

    # Act
    watering_schedule.schedule_watering(scheduled_watering)

    # Assert
    assert watering_schedule._exists() is True

    scheduled_watering_stored = watering_schedule.select().loc[0, :].to_dict()

    for key, value in scheduled_watering_stored.items():
        if key in ['id', 'last_triggered_utc']:
            pass
        elif key in ['insert_datetime_utc']:
            assert value == str(scheduled_watering[key])
        else:
            assert value == scheduled_watering[key]

def test_check_should_water(tmp_path):
    # Arange
    path = tmp_path

    database_sqlite = DatabaseSqlite(tmp_path, COMMUNICATION_DB_NAME_TEST)
    watering_schedule = WateringSchedule(database_sqlite)

    now = pd.Timestamp.utcnow()
    scheduled_watering = {'insert_datetime_utc': now.to_pydatetime(),
                          'channel': 1,
                          'start_time_utc': '10:00',
                          'end_time_utc': '20:00',
                          'weekday': now.weekday() + 1,
                         }

    watering_schedule.schedule_watering(scheduled_watering)

    # Act
    should_water = watering_schedule.check_should_water(pd.to_datetime('11:00'))

    # Assert
    assert should_water is True

def test_check_should_water_dont_water(tmp_path):
    # Arange
    path = tmp_path

    database_sqlite = DatabaseSqlite(tmp_path, COMMUNICATION_DB_NAME_TEST)
    watering_schedule = WateringSchedule(database_sqlite)

    now = pd.Timestamp.utcnow()
    scheduled_watering = {'insert_datetime_utc': now.to_pydatetime(),
                          'channel': 1,
                          'start_time_utc': '10:00',
                          'end_time_utc': '20:00',
                          'weekday': now.weekday() + 1,
                         }

    watering_schedule.schedule_watering(scheduled_watering)

    # Act
    should_water = watering_schedule.check_should_water(pd.to_datetime('21:00'))

    # Assert
    assert should_water is False
