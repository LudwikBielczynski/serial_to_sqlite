import json

from kivy.app import App

import widgets.state

from widgets.info_bubble import print_on_info_bubble
from widgets.login.login import validate_login_and_relays_data

def maybe_switch_to_relay_controller(dt):
    if widgets.state.login_transition:
        validate_login_and_relays_data()

def to_control(revert=True):
    if revert:
        widgets.state.relay = widgets.state.relay_cache
        widgets.state.relays = widgets.state.relays_cache
           
    app = App.get_running_app()
    app.screen_manager.transition.direction = 'right'
    app.screen_manager.current = 'relay_controller'

def save_to_control():
    screen = App.get_running_app() \
                .screen_manager \
                .get_screen('relay_settings')

    widgets.state.relay = {
        'channel': int(screen.channel_input.text),
        'section_name': screen.relay_name_input.text,
        'start': screen.start_time_input.text,
        'end': screen.end_time_input.text,
        'weekdays': json.loads(screen.weekday_input.text),
    }

    to_control(revert=False)
    print_on_info_bubble('Saved')
