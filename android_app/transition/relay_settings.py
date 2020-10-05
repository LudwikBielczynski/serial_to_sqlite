from kivy.app import App

def to_relay_settings(instance):
    app = App.get_running_app()
    app.screen_manager.transition.direction = 'left'
    app.screen_manager.current = 'relay_settings'
