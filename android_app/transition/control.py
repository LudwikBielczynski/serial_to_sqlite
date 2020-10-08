import json

from kivy.app import App

import widgets.state

def to_control():

    app = App.get_running_app()
    app.screen_manager.transition.direction = 'right'
    app.screen_manager.current = 'control'

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

    to_control()
