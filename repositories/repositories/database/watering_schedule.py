import pandas as pd
from typing import Dict

from repositories.database.sqlite import Table

class WateringSchedule(Table):
    name = 'watering_schedule'
    meta = [('insert_datetime_utc', 'DATETIME', 'NOT NULL'),
            ('channel', 'INTEGER', 'NOT NULL'),
            ('start_time_utc', 'TEXT', 'NOT NULL'),
            ('end_time_utc', 'TEXT', 'NOT NULL'),
            ('weekday', 'INTEGER', 'NULL'),
            ('last_triggered_utc', 'DATETIME', 'NULL'),
           ]

    def schedule_watering(self,
                          columns_values_map: Dict[str, str],
                         ) -> None:
        super().insert(columns_values_map)

    def check_should_water(self, channel: int, now_utc: pd.Timestamp) -> bool:
        # Pandas weekday format is 0-6 Mo-Su, preferred on is 1-7
        weekday = now_utc.weekday() + 1

        cases = f'''
            channel = {channel}
            AND start_time_utc < '{now_utc.strftime("%H:%M")}'
            AND end_time_utc > '{now_utc.strftime("%H:%M")}'
            AND weekday = {weekday}
            '''
        tasks = super().select(cases=cases)

        if tasks.empty:
            return False
        else:
            return True

    def check_if_already_scheduled(self,
                                   channel: int,
                                   weekday: int
                                  ) -> bool:
        '''Watering should be only sceduled once per day per section'''
        cases = f'''
            channel = {channel}
            AND weekday = {weekday}
            '''
        tasks = super().select(cases=cases)

        if tasks.empty:
            return False
        else:
            return True

    def delete_for_channel_weekday_schedule(self, channel: int, weekday: int) -> None:
        '''Needed to clean the data for a specific channel and weekday combination'''
        cases = f'''
            channel = {channel}
            AND weekday = {weekday}
            '''
        super().delete(cases=cases)

    def delete_for_channel_schedule(self, channel: int) -> None:
        '''Needed to clean the data for a specific channel'''
        cases = f'''
            channel = {channel}
            '''
        super().delete(cases=cases)

    def get_all_schedule(self):
        '''Function needed for the UI'''
        return super().select()
