from common.shares import LOCAL_DATABASES_PATH
from repositories.database import WateringSchedule
from repositories.database.sqlite import DatabaseSqlite

if __name__ == '__main__':
    LOCAL_DATABASES_PATH.mkdir(parents=True, exist_ok=True)

    # Create database and initialize objects to handle operations on tables
    database_sqlite = DatabaseSqlite(LOCAL_DATABASES_PATH, 'watering_schedule.db')
    soil_humidity_table = WateringSchedule(database_sqlite)

