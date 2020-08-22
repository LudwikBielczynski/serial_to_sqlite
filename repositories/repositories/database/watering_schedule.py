from repositories.database.sqlite import Table

class WateringSchedule(Table):
    name = 'watering_schedule'
    meta = [('insert_datetime_utc', 'TEXT', 'NOT NULL'),
            ('section', 'TEXT', 'NOT NULL'),
            ('channel', 'TEXT', 'NOT NULL'),
            ('start_time_utc', 'TEXT', 'NOT NULL'),
            ('end_time_utc', 'TEXT', 'NOT NULL'),
            ('weekday', 'TEXT', 'NULL'),
            ('last_triggered_utc', 'TEXT', 'NULL'),
           ]
