from kivy.app import App

import widgets.state

def logout():
    widgets.state.relays = []
    widgets.state.username = ''
    widgets.state.password = ''

    app = App.get_running_app()
    app.screen_manager.transition.direction = 'right'
    app.screen_manager.current = 'login'
