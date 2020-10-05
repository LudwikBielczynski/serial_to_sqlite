from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.factory import Factory

def print_on_info_bubble(self, message):
    message = repr(message)
    root = App.get_running_app().root
    if not root.current_screen.ids.info_bubble:
        info_bubble = Factory.InfoBubble()
    root.current_screen.ids.info_bubble.message = message

    # Check if bubble is not already on screen
    if not root.current_screen.ids.info_bubble.parent:
        Window.add_widget(root.current_screen.ids.info_bubble)

    # Remove bubble after 2 secs
    Clock.schedule_once(lambda dt:
        Window.remove_widget(root.current_screen.ids.info_bubble), 2)
