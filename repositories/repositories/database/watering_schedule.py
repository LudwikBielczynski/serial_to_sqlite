from repositories.database.sqlite import Table

class WateringSchedule(Table):
    name = 'watering_schedule'
    meta = [('insert_datetime', 'TEXT', 'NOT NULL'),
            ('section', 'TEXT', 'NOT NULL'),
            ('channel', 'TEXT', 'NOT NULL'),
            ('start', 'TEXT', 'NOT NULL'),
            ('end', 'TEXT', 'NOT NULL'),
            ('weekday', 'TEXT', 'NULL'),
           ]
