from dataclasses import dataclass
from datetime import datetime
import sqlite3
from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Optional, Tuple, Union

import pandas as pd

if TYPE_CHECKING:
    from pathlib import Path, PosixPath, WindowsPath
    from sqlite3 import Connection

@dataclass
class DatabaseSqlite:
    path: Union['Path', 'PosixPath', 'WindowsPath']
    name: str

    def __post_init__(self):
        self.connection = self.connect()

    def connect(self) -> 'Connection':
        '''
        Function connecting to the local sqlite database occupying a selected folder.

        If the database does not exist it is created. The only necessary condition is the existence of
        the path. The creation of the folder is not added in this function as in the production
        environment it will be the bare folder shared between ETL and forecasting/predictive
        applications, and we don't want to create confusion by mistakenly creating a folder which could
        be local.
        '''
        return sqlite3.connect(self.path / self.name)

    def refresh(self) -> None:
        self.connection = self.connect()

class Table():
    '''A general class which will be inherited to access and manipulate each sqlite table.'''
    name = 'name'

    # meta should be a list of tuples [(column, column_type, nullable)]
    # e.g. [("insert_datetime_utc", "TEXT", "NOT NULL")]
    meta: List[Tuple[str, str, str]]

    def __init__(self,
                 database: 'DatabaseSqlite'
                ) -> None:
        self.database = database

    def refresh(self):
        self.database.refresh()

    @property
    def meta_columns(self):
        return [column_meta[0] for column_meta in self.meta]

    def _check_new_columns(self, columns_new: Iterable[str]) -> None:
        '''Function used to check if needed columns are coherent with the table meta'''
        unknown_columns = set(columns_new) - set(self.meta_columns)

        if unknown_columns:
            raise AttributeError(f'Not known meta for columns: {unknown_columns}')

    def _exists(self) -> bool:
        query = f'''
            SELECT name
                FROM sqlite_master
                WHERE type='table'
                    AND name='{self.name}'
            '''
        cursor = self.database.connection.execute(query)
        result = cursor.fetchone()
        return result is not None

    def _create(self) -> None:
        '''Function that creates the table with the meta'''
        query = f'''
            CREATE TABLE {self.name} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        '''
        for (column, column_type, nullable) in self.meta:
            query += f'{column} {column_type} {nullable}, '
        query = query[:-2] + ');'
        self.database.connection.execute(query)
        self.database.connection.commit()

    def select(self,
               columns: Optional[List[str]] = None,
               cases: str = ''
              ) -> pd.DataFrame:
        '''Function used to select the data'''
        if not self._exists():
            self._create()

        query = 'SELECT '
        if columns is None:
            query += '* '
        else:
            self._check_new_columns(columns)
            query += ','.join(columns)

        query += f' FROM {self.name} '
        if cases:
            query += f'WHERE {cases}'
        query += ';'
        cursor = self.database.connection.execute(query)

        results = cursor.fetchall()

        # Format data before export
        if columns:
            results_df = pd.DataFrame(results, columns=columns)
        else:
            columns = ['id']
            columns.extend(self.meta_columns)
            results_df = pd.DataFrame(results, columns=columns)

        return results_df

    def insert(self, columns_values_map: Dict[str, str]) -> None:
        '''Function that inserts a row to the table'''
        if not self._exists():
            self._create()

        self._check_new_columns(columns_values_map.keys())
        cursor = self.database.connection.cursor()
        query = f'INSERT INTO {self.name} ('
        query += ','.join(columns_values_map.keys())
        query += ') VALUES ('
        query += '?,' * len(columns_values_map.keys())
        query = query[:-1] + ');'

        # TODO: Change if multirow comits should be enabled
        values = [tuple(columns_values_map.values())]
        cursor.executemany(query, values)
        self.database.connection.commit()

    def delete(self, cases: str = '', force: bool = False) -> pd.DataFrame:
        '''Function used to delete a selected row'''
        if (cases == '') & (force is False):
            raise AttributeError('Any case must be given otherwise the table will be empty')

        cursor = self.database.connection.cursor()
        query = f'DELETE FROM {self.name} '
        query += f'WHERE {cases}'
        query += ';'
        cursor = self.database.connection.execute(query)
        self.database.connection.commit()

    def update(self,
               columns_values_map: Dict[str, str],
               cases: str,
               order_columns: List[str],
               limit: int) -> None:
        '''Function used to update a seleted row'''
        self._check_new_columns(columns_values_map.keys())
        cursor = self.database.connection.cursor()
        query = f'UPDATE {self.name} SET '

        for column, value in columns_values_map.items():
            query += f"{column} = '{value}', "

        query = query[:-2] + f" WHERE {cases} ORDER BY {','.join(order_columns)} LIMIT {limit};"
        cursor = self.database.connection.execute(query)
        self.database.connection.commit()
