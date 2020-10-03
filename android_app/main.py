from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from widgets.weedays_popup import WeekdaysPopupLayout
from widgets.relay_controler import RelayControlersLayout
from widgets.settings import SettingsContent
import widgets.state

# TODO: Save tz info?
# time.strftime('%z')
# datetime.strptime('20:00+0200', '%H:%M%z')

# TODO: Implement multi screen layout
# https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html

# TODO: Implement manual turning on and off

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
        # SettingsContent
        #     size: root.width * 0.8, root.height * 0.8
        #     row_force_default: True
        #     row_default_height: 50
        #     center: root.width / 2, root.height / 2
                    
        #     Button:
        #         text: 'Log in'
        #         on_press:
        #             login()
    # AnchorLayout:
    #     anchor_x: 'center'
    #     anchor_y: 'center'
Builder.load_string("""
#:import SettingsContent widgets.settings.SettingsContent
#:import login widgets.settings.login
<LoginScreen>:

    RelativeLayout:
        size_hint: None, None
        size: root.width, root.height / 5
        pos: 0, root.height / 2 - root.height / (5 * 2)
        BoxLayout:
            orientation: 'vertical'
            nrows: 2

            Button:
                text: 'Log in'
            Button:
                text: 'Log in2'

<ControlScreen>:
    GridLayout:
        nrows: 1
        Button:
            text: 'Log out'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'login'
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

WateringControlSystemApp().run()
