from typing import Any, Dict, List

from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import requests

import widgets.state

def login(instance):
  # TODO: Authentication

  url = f'http://{widgets.state.host}:5000/get_relay_configuration'
  response = requests.get(url=url)
  channel_section_name_map = response.json()

  url = f'http://{widgets.state.host}:5000/get_schedule'
  response = requests.get(url=url)
  schedules = response.json()

  def format_relays_data(channel_section_name_map: Dict[str, str],
                         schedules: Dict[str, Dict[str, Any]]
                        ) -> List[Dict[str, Any]]:
    '''Function needed to reformat data from the relay_sceduler to the android API'''
    def create_default_realy(channel: str, section_name: str) -> Dict[str, Any]:
      return {
          'channel': int(channel),
          'section_name': section_name,
          'start': '19:00',
          'end': '19:15',
          'weekdays': []
          }
    relays = [create_default_realy(channel, section_name)
              for channel, section_name in channel_section_name_map.items()]

    if schedules:
      for schedule in schedules.values():
        for relay_nr, relay_default in enumerate(relays):
          if relay_default['channel'] == schedule['channel']:
            relays[relay_nr]['start'] = schedule['start_time_utc']
            relays[relay_nr]['end'] = schedule['end_time_utc']
            relays[relay_nr]['weekdays'].append(schedule['weekday'])

    return relays

  widgets.state.relays = format_relays_data(channel_section_name_map, schedules)

  # widgets.state.relays = [
  #   {'channel': 1, 'section_name': 'Relay 1', 'start': '18:00', 'end': '20:00', 'weekdays': [1]},
  #   {'channel': 2, 'section_name': 'Relay 1', 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
  #   {'channel': 3, 'section_name': 'Relay 1', 'start': '18:00', 'end': '20:00', 'weekdays': [2, 4, 6]},
  #   {'channel': 4, 'section_name': 'Relay 1', 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
  #   ]

class SettingsPopupContent(GridLayout):

  def __init__(self, **kwargs):
    super(SettingsPopupContent, self).__init__(**kwargs)
    self.rows = 4

    self.add_widget(Label(text='Host'))
    self.host_input = TextInput(text=widgets.state.host, multiline=False)
    def on_host_input(instance, value):
      widgets.host = value
    self.host_input.bind(text=on_host_input)
    self.add_widget(self.host_input)

    self.add_widget(Label(text='User Name'))
    self.username_input = TextInput(text=widgets.state.username, multiline=False)
    def on_username_input(instance, value):
      widgets.username = value
    self.username_input.bind(text=on_username_input)
    self.add_widget(self.username_input)

    self.add_widget(Label(text='Password'))
    self.password_input = TextInput(text=widgets.state.password, password=True, multiline=False)
    def on_password_input(instance, value):
      widgets.password = value
    self.password_input.bind(text=on_password_input)
    self.add_widget(self.password_input)

    self.add_widget(Label(text=''))
    self.button_login = Button(text='Log in',
                               on_release=login
                              )
    self.add_widget(self.button_login)

class SettingsPopupLayout(AnchorLayout):

  def __init__(self, **kwargs):
    super(SettingsPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)
    settings_popup_content = SettingsPopupContent()
    self.popup = Popup(title='Settings',
                       content=settings_popup_content,
                       size_hint=(None, None),
                       size=(Window.width*0.9, Window.height*0.3),
                      )