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

Builder.load_string("""
#:import login widgets.login.login
#:import state widgets.state
<LoginScreen>:

    RelativeLayout:
        size_hint: None, None
        size: root.width, root.height / 4
        pos: 0, root.height / 2 - root.height / (4 * 2)
        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Watering system'

            BoxLayout:
                orientation: 'horizontal'

                Label:
                    text: 'Host'

                TextInput:
                    id: host_name
                    text: state.host
                    multiline: False
                    on_text:
                        app.set_state_host()

            BoxLayout:
                orientation: 'horizontal'

                Label:
                    text: 'Username'

                TextInput:
                    id: username
                    text: state.username
                    multiline: False
                    on_text:
                        app.set_state_username()

            BoxLayout:
                orientation: 'horizontal'

                Label:
                    text: 'Password'

                TextInput:
                    id: password
                    text: state.password
                    password: True
                    multiline: False
                    on_text:
                        app.set_state_password()

            BoxLayout:
                orientation: 'horizontal'

                Label:
                    text: ''

                Button:
                    text: 'Login'
                    on_press:
                        login()

#:import RelayControlersLayout widgets.relay_controler.RelayControlersLayout
<ControlScreen>:
    RelayControlersLayout
     
""")


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
