from copy import deepcopy

from kivy.app import App

import widgets.state

def to_relay_settings(instance):
    app = App.get_running_app()

    # Create a cache of relays settings, so that the changes can be reverted
    widgets.state.relays_cache = deepcopy(widgets.state.relays)
    widgets.state.relay_cache = deepcopy(instance.relay)
    
    # This relay will be changed on the settings screen
    widgets.state.relay = instance.relay
    
    # Display relay wich will be modified
    relay_settings_screen = app.screen_manager.get_screen('relay_settings')
    relay_settings_screen.channel_input.text = str(widgets.state.relay['channel'])
    relay_settings_screen.relay_name_input.text = widgets.state.relay['section_name']
    relay_settings_screen.start_time_input.text = widgets.state.relay['start']
    relay_settings_screen.end_time_input.text = widgets.state.relay['end']
    relay_settings_screen.weekday_input.text = str(widgets.state.relay['weekdays'])

    # Transition
    app.screen_manager.transition.direction = 'left'
    app.screen_manager.current = 'relay_settings'
