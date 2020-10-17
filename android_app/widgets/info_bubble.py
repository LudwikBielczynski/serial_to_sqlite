from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.factory import Factory

def print_on_info_bubble(message):
    message = repr(message)
    app = App.get_running_app()
    # screen = app.screen_manager.get_screen('login')
    # screen = app.screen_manager.get_screen('relay_controller')
    screen = app.screen_manager.current_screen
    # if not app.root.current_screen.ids.info_bubble:
    # screen.ids.info_bubble = Factory.InfoBubble()
    screen.ids.info_bubble.text = message
    # app.root.current_screen.ids.info_bubble.text = repr('dupa')
    # app.root.current_screen.ids.info_bubble.text = message
    screen.info_bubble.text = message
    
    # Remove bubble after 2 secs
    # Clock.schedule_once(lambda dt:
    #     Window.remove_widget(screen.ids.info_bubble), 2)

    # if not app.root.current_screen.ids.info_bubble:
    #     relay_controller_screen.ids.info_bubble = Factory.InfoBubble()

    # # app.root.screens.ids.info_bubble.message = message

    # # Check if bubble is not already on screen
    # if not app.root.current_screen.ids.info_bubble.parent:
    #     Window.add_widget(app.root.current_screen.ids.info_bubble)

    # # Remove bubble after 2 secs
    # Clock.schedule_once(lambda dt:
    #     Window.remove_widget(app.root.current_screen.ids.info_bubble), 2)
