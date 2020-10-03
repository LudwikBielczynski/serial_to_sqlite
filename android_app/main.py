from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from widgets.weedays_popup import WeekdaysPopupLayout
from widgets.relay_controler import RelayControlersLayout
import widgets.state

# TODO: Save tz info?
# time.strftime('%z')
# datetime.strptime('20:00+0200', '%H:%M%z')

# TODO: Implement multi screen layout
# https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html

# TODO: Implement manual turning on and off
Builder.load_file('screen/login.kv')
Builder.load_file('screen/control.kv')

# Declare both screens
class LoginScreen(Screen):
    pass

class ControlScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(ControlScreen(name='control'))

class WateringControlSystemApp(App):

    def build(self):
        # root = RootScreen()
        return sm

    def set_state_host(self):
        widgets.state.host = self.root.current_screen.ids.host_name.text

    def set_state_username(self):
        widgets.state.username = self.root.current_screen.ids.username.text

    def set_state_password(self):
        widgets.state.password = self.root.current_screen.ids.password.text

WateringControlSystemApp().run()
