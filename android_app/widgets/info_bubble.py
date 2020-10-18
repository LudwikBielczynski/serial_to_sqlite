import threading

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.factory import Factory

def update_info_bubble(screen, message):
    # If info bubble was not initialized before
    if not hasattr(screen, 'info_bubble'):
        screen.info_bubble = Factory.InfoBubble()

    # If the info bubble is not currently shown it does not have any parents
    if screen.info_bubble.parent is None:
        screen.add_widget(screen.info_bubble)
        screen.info_bubble.message = ''

    # The message should be appended if the bubble is already present
    if hasattr(screen.info_bubble, 'message'):
        if screen.info_bubble.message:
            screen.info_bubble.message += '\n'
        screen.info_bubble.message += message.replace("'", '')
    else:
        screen.info_bubble.message = message

    # Remove bubble after few secs
    Clock.schedule_once(lambda dt: screen.remove_widget(screen.info_bubble), 15)

def print_on_info_bubble(message):
    print(message)
    message = repr(message)
    app = App.get_running_app()
    screen = app.screen_manager.current_screen

    for screen_name in app.screen_manager.screen_names:
        screen = app.screen_manager.get_screen(screen_name)
        update_info_bubble(screen, message)
