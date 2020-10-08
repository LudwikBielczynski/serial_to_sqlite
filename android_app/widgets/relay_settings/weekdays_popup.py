import json
from typing import Callable, List, Optional

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch

import widgets.state
from widgets.share import WEEKDAYS_MAPPING

class WeekdaySwitch(Switch):

    def __init__(self, weekday: str, **kwargs):
        super(WeekdaySwitch, self).__init__(**kwargs)
        self.weekday = weekday

def update_relays_state(instance, value):

    relay_to_modify = [relay
                      for relay in widgets.state.relays
                      if relay['channel'] == widgets.state.relay['channel']
                      ][0]

    if value:
        relay_to_modify['weekdays'].append(WEEKDAYS_MAPPING[instance.weekday])
    else:
        relay_to_modify['weekdays'].remove(WEEKDAYS_MAPPING[instance.weekday])
    relay_to_modify['weekdays'].sort()

    print(relay_to_modify)
    for idx, relay in enumerate(widgets.state.relays):
        if relay['channel'] == widgets.state.relay['channel']:
            widgets.state.relays[idx] = relay_to_modify

    widgets.state.relay = relay_to_modify

class WeekdaysPopupContent(GridLayout):

    def __init__(self, **kwargs):
        super(WeekdaysPopupContent, self).__init__(**kwargs)
        self.columns = 2
        self.rows = 7

        self.weekday_switches = {}

        for weekday in WEEKDAYS_MAPPING.keys():
            self.add_widget(Label(text=weekday))

            if WEEKDAYS_MAPPING[weekday] in widgets.state.relay['weekdays']:
                active = True
            else:
                active = False

            weekday_switch = WeekdaySwitch(weekday, active=active)
            weekday_switch.bind(active=update_relays_state)

            self.weekday_switches[weekday] = weekday_switch
            self.add_widget(self.weekday_switches[weekday])

def update_relay_control_labels(*args):
    relay_settings_screen = App.get_running_app() \
                               .screen_manager \
                               .get_screen('relay_settings')
    relay_settings_screen.weekday_input.text = str(widgets.state.relay['weekdays'])

class WeekdaysPopupLayout(AnchorLayout):

    def __init__(self, **kwargs):
        super(WeekdaysPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)

        weekdays_popup_content = WeekdaysPopupContent()
        self.popup = Popup(title='Select weekdays',
                           content=weekdays_popup_content,
                           size_hint=(None, None),
                           size=(Window.width*0.9, Window.height*0.45),
                          )
        self.popup.bind(on_dismiss=update_relay_control_labels)