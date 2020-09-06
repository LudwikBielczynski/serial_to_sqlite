from json.decoder import JSONDecodeError
from typing import Any, Dict, List, Optional

import requests
from requests.exceptions import ConnectionError
from urllib3.connection import NewConnectionError

import widgets.state

class WateringSchedulerCommunicator:

    def __init__(self, host: str):
        self.host = host
        self.channel_section_name_map = {} # type: Dict[str, str]
        self.schedules = {} # type: Dict[str, Dict[str, Any]]
    def fetch_data_from_host(self):
        try:
            self.channel_section_name_map = self._get_relay_configuration()
            self.schedules = self._get_schedule()
        except (ConnectionError, NewConnectionError, JSONDecodeError):
            pass

    def _get_relay_configuration(self) -> Dict[str, str]:
        url = f'http://{self.host}:5000/get_relay_configuration'
        response = requests.get(url=url, timeout=5, auth=(widgets.state.username, widgets.state.password))
        return response.json()

    def _get_schedule(self) -> Dict[str, Dict[str, Any]]:
        url = f'http://{self.host}:5000/get_schedule'
        response = requests.get(url=url, timeout=5, auth=(widgets.state.username, widgets.state.password))
        return response.json()

    def get_formatted_relays_data(self):
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

        if self.schedules:
            for schedule in self.schedules.values():
                for relay_nr, relay_default in enumerate(relays):
                    if relay_default['channel'] == schedule['channel']:
                        relays[relay_nr]['start'] = schedule['start_time_utc']
                        relays[relay_nr]['end'] = schedule['end_time_utc']
                        relays[relay_nr]['weekdays'].append(schedule['weekday'])

        return relays

    def delete_all_schedule(self, relays: List[Dict[str, Any]]) -> None:
        for relay in relays:
            try:
                url = f"http://{self.host}:5000/delete_for_channel_watering_schedule/{relay['channel']}"
                response = requests.put(url=url, timeout=5, auth=(widgets.state.username, widgets.state.password))
                print(response.text)
            except ConnectionError:
                pass

    def send_all_schedule_to_host(self, relays: List[Dict[str, Any]]) -> None:
        def format_time(time: str) -> str:
            if len(time.split(':')[0]) == 1:
                time = f'0{time}'
            return time

        for relay in relays:
            if relay['weekdays']:
                for weekday in relay['weekdays']:
                    print(relay)
                    channel = relay['channel']
                    start_time_utc = format_time(relay['start'])
                    end_time_utc = format_time(relay['end'])

                    try:
                        url = f'http://{self.host}:5000/schedule_watering/{channel}_{start_time_utc}-{end_time_utc}_{weekday}'
                        response = requests.put(url=url, timeout=5, auth=(widgets.state.username, widgets.state.password))
                        print(response.text)
                    except ConnectionError:
                        pass
