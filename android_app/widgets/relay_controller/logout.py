from kivy.app import App

import widgets.state

def logout():
    widgets.state.relay = {'channel': 0
                          }
    widgets.state.relays = []
    widgets.state.username = ''
    widgets.state.password = ''

    app = App.get_running_app()

    screen = app.screen_manager.get_screen('relay_controller')
    screen.relay_controller_layout.update_relay_widgets()

    app.screen_manager.transition.direction = 'right'
    app.screen_manager.current = 'login'