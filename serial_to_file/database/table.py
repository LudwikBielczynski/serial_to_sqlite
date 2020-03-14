from datetime import datetime
from typing import TYPE_CHECKING

from serial_to_sqlite.database.wrappers import execute_and_commit

if TYPE_CHECKING:
    from sqlite3 import Connection

class Table():
    name = 'name'

    def __init__(self, connection: 'Connection'):
        self.connection = connection

    def exists(self):
        query = f'''
            SELECT name
                FROM sqlite_master
                WHERE type='table'
                    AND name='{self.name}'
            '''
        cursor = self.connection.execute(query)
        result = cursor.fetchone()
        return result is not None

    @execute_and_commit
    def create(self):
        '''Function that creates the table where soil humidity data is stored'''
        query = f'''
            CREATE TABLE {self.name} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                insert_datetime TEXT NOT NULL,
                transmitter_name TEXT NOT NULL,
                sensor_value REAL NULL
                );
        '''
        return query

    def insert(self, transmitter_name, sensor_value):
        '''Function that inserts battery state data'''
        cursor = self.connection.cursor()
        query = f'''
            INSERT INTO {self.name}
                (insert_datetime,
                 transmitter_name,
                 sensor_value
                )
                VALUES (?,?,?)
        '''
        values = [(datetime.now(), transmitter_name, sensor_value)]
        cursor.executemany(query, values)
        self.connection.commit()
