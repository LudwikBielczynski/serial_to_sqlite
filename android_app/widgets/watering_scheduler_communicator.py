from datetime import datetime
from json.decoder import JSONDecodeError
import time
from typing import Any, Dict, List, Optional

import requests
from requests.exceptions import ConnectionError
from urllib3.connection import NewConnectionError, ConnectTimeoutError

import widgets.state
from widgets.info_bubble import print_on_info_bubble

TIMEOUT_TIME = 5

CLIENT_TZ_STR = time.strftime('%z')
CLIENT_TZ = datetime.strptime(CLIENT_TZ_STR, '%z').tzinfo

class WateringSchedulerCommunicator:

    def __init__(self, host: str):
        self.host = host
        self.channel_section_name_map = {} # type: Dict[str, str]
        self.schedules = {} # type: Dict[str, Dict[str, Any]]

    def fetch_data_from_host(self):
        if widgets.state.DEBUG:
            widgets.state.login_transition = True

        try:
            waiting_counter = 0
            while (widgets.state.communicator != 'free') & (waiting_counter <= TIMEOUT_TIME):
                time.sleep(1)
                waiting_counter += 1

            if waiting_counter == TIMEOUT_TIME:
                raise ConnectTimeoutError

            widgets.state.communicator = 'fetched_data_from_host'
            self.channel_section_name_map = self._get_relay_configuration()
            self.schedules = self._get_schedule()
            widgets.state.login_transition = True

        except (ConnectionError, NewConnectionError, JSONDecodeError, ConnectTimeoutError) as msg:
            widgets.state.communicator = 'free'
            print_on_info_bubble('Could not connect to host')

    def _get_relay_configuration(self) -> Dict[str, str]:
        url = f'http://{self.host}:5000/get_relay_configuration'
        response = requests.get(url=url, timeout=TIMEOUT_TIME, auth=(widgets.state.username, widgets.state.password))
        return response.json()

    def _get_schedule(self) -> Dict[str, Dict[str, Any]]:
        url = f'http://{self.host}:5000/get_schedule'
        response = requests.get(url=url, timeout=TIMEOUT_TIME, auth=(widgets.state.username, widgets.state.password))
        return response.json()

    def format_relays_data(self):
        def create_default_relay(channel: str,
                                 section_name: str
                                ) -> Dict[str, Any]:
            return {'channel': int(channel),
                    'section_name': section_name,
                    'start': '19:00',
                    'end': '19:15',
                    'weekdays': []
                    }
        relays = [create_default_relay(channel, section_name)
                  for channel, section_name in self.channel_section_name_map.items()]

        def normalize_time(time_str):
            if '+' in time_str: 
                if time_str[-5:] != CLIENT_TZ:
                    time_tz = datetime.strptime(time_str, '%H:%m%z')
                    time_tz = time_tz.astimezone(CLIENT_TZ)
                    time_str = time_tz.strftime('%H:%m%z')
                    
            return time_str
            
        if self.schedules:
            for schedule in self.schedules.values():
                for relay_nr, relay_default in enumerate(relays):
                    if relay_default['channel'] == schedule['channel']:
                        relays[relay_nr]['start'] = normalize_time(schedule['start_time_utc'])
                        relays[relay_nr]['end'] = normalize_time(schedule['end_time_utc'])
                        relays[relay_nr]['weekdays'].append(schedule['weekday'])

        return relays

    def delete_all_schedule(self, relays: List[Dict[str, Any]]) -> None:
        for relay in relays:
            try:
                url = f"http://{self.host}:5000/delete_for_channel_watering_schedule/{relay['channel']}"
                response = requests.put(url=url, timeout=15, auth=(widgets.state.username, widgets.state.password))
                print(response.text)
            except ConnectionError:
                pass

    def send_all_schedule_to_host(self, relays: List[Dict[str, Any]]) -> None:
        def format_time(time_str: str) -> str:
            if len(time_str.split(':')[0]) == 1:
                time_str = f'0{time_str}'
            return time_str + CLIENT_TZ_STR

        for relay in relays:
            if relay['weekdays']:
                for weekday in relay['weekdays']:
                    print(relay)
                    channel = relay['channel']
                    start_time_utc = format_time(relay['start'])
                    end_time_utc = format_time(relay['end'])

                    try:
                        url = f'http://{self.host}:5000/schedule_watering/{channel}_{start_time_utc}-{end_time_utc}_{weekday}'
                        response = requests.put(url=url, timeout=15, auth=(widgets.state.username, widgets.state.password))
                        print(response.text)
                    except ConnectionError:
                        pass
