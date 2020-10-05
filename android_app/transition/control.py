from kivy.app import App

def to_control():
    app = App.get_running_app()
    app.screen_manager.transition.direction = 'right'
    app.screen_manager.current = 'control'
