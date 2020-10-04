from kivy.app import App

import widgets.state

def logout():
    widgets.state.relays = []
    widgets.state.username = ''
    widgets.state.password = ''

    manager = App.get_running_app().root
    manager.transition.direction = 'right'
    manager.current = 'login'
