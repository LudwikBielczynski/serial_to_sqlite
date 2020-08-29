from typing import Any, Dict, List

import requests

class WateringSchedulerCommunicator:

    def __init__(self, host: str):
        self.host = host

        self.channel_section_name_map = self._get_relay_configuration()
        self.schedules = self._get_schedule()

    def _get_relay_configuration(self) -> Dict[str, str]:
        url = f'http://{self.host}:5000/get_relay_configuration'
        response = requests.get(url=url, timeout=5)
        return response.json()

    def _get_schedule(self) -> Dict[str, Dict[str, Any]]:
        url = f'http://{self.host}:5000/get_schedule'
        response = requests.get(url=url, timeout=5)
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
                response = requests.put(url=url, timeout=5)

            except ConnectionError:
                pass

    def send_all_schedule_to_host(self, relays: List[Dict[str, Any]]) -> None:
        print(relays)

