from serial_to_sqlite.database.table import Table
from serial_to_sqlite.database.wrappers import execute_and_commit

class SoilHumidityTable(Table):
    name = 'soil_humidity'
