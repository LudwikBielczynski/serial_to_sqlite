from kivy.app import App

from widgets.info_bubble import print_on_info_bubble
import widgets.state

def logout():
    widgets.state.relay = {'channel': 0
                          }
    widgets.state.relays = []
    widgets.state.username = ''
    widgets.state.password = ''

    app = App.get_running_app()

    screen = app.screen_manager.get_screen('relay_controller')
    screen.relay_controller_layout.remove_widgets()

    app.screen_manager.transition.direction = 'right'
    app.screen_manager.current = 'login'

    print_on_info_bubble('Logged out')
