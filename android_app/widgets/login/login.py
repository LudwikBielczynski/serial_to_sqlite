import time
from typing import Any, Dict, List

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
import requests
from requests.exceptions import ConnectionError

import widgets.state
from widgets.watering_scheduler_communicator import WateringSchedulerCommunicator
from widgets.info_bubble import print_on_info_bubble

def login():
    communicator = WateringSchedulerCommunicator(widgets.state.host)
    try:
        # communicator.fetch_data_from_host()
        # widgets.state.relays = communicator.get_formatted_relays_data()
        print_on_info_bubble('Logged in')

        # DEBUG: Mock some data for debug
        widgets.state.relays = [
            {'channel': 1, 'section_name': 'Relay 1', 'start': '18:00', 'end': '20:00', 'weekdays': [1]},
            {'channel': 2, 'section_name': 'Relay 1', 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
            {'channel': 3, 'section_name': 'Relay 1', 'start': '18:00', 'end': '20:00', 'weekdays': [2, 4, 6]},
            {'channel': 4, 'section_name': 'Relay 1', 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
            ]

        if widgets.state.relays:
            app = App.get_running_app()
            app.screen_manager.transition.direction = 'left'
            app.screen_manager.current = 'relay_controller'
        else:
            raise AttributeError

    except ConnectionError:
        print_on_info_bubble('Could not fetch data')

    except AttributeError:
        print_on_info_bubble('Data from host empty')

