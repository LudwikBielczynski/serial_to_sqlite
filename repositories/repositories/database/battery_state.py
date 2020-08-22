from repositories.database.sqlite import Table

class BatteryStateTable(Table):
    name = 'battery_state'
    meta = [('insert_datetime', 'TEXT', 'NOT NULL'),
            ('transmitter_name', 'TEXT', 'NOT NULL'),
            ('sensor_value', 'REAL', 'NULL'),
           ]
