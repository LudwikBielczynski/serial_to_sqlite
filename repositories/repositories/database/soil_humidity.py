from repositories.database.sqlite import Table

class SoilHumidityTable(Table):
    name = 'soil_humidity'
    meta = [('insert_datetime', 'TEXT', 'NOT NULL'),
            ('transmitter_name', 'TEXT', 'NOT NULL'),
            ('sensor_value', 'REAL', 'NULL'),
           ]