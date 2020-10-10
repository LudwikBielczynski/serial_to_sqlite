from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import widgets.state
from widgets.relay_settings.weekdays_popup import WeekdaysPopupLayout

# TODO: Save tz info?
# time.strftime('%z')
# datetime.strptime('20:00+0200', '%H:%M%z')
# TODO: Implement logs bubble for logs
# TODO: Implement manual relay turning on and off
# TODO: Reset relays on logout
# TODO: Validate input on relay settings screen

# Declare both screens
Builder.load_file('screen/login.kv')
class LoginScreen(Screen): ...

Builder.load_file('screen/relay_controller.kv')
class RelayControllerScreen(Screen): ...

Builder.load_file('screen/relay_settings.kv')
class RelaySettingsScreen(Screen):

    def open_weekday_popup(self):
        popup_layout = WeekdaysPopupLayout()
        popup_layout.popup.open()

# Create the screen manager
class WateringControlSystemScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(WateringControlSystemScreenManager, self).__init__(**kwargs)

        self.login_screen = self.add_widget(LoginScreen(name='login'))
        self.control_screen = self.add_widget(RelayControllerScreen(name='relay_controller'))
        self.relay_settings = self.add_widget(RelaySettingsScreen(name='relay_settings'))

class WateringControlSystemApp(App):

    def build(self):
        self.screen_manager = WateringControlSystemScreenManager()
        return self.screen_manager

    def set_state_host(self):
        widgets.state.host = self.root.current_screen.ids.host_name.text

    def set_state_username(self):
        widgets.state.username = self.root.current_screen.ids.username.text

    def set_state_password(self):
        widgets.state.password = self.root.current_screen.ids.password.text

if __name__ == '__main__':
    app = WateringControlSystemApp()
    app.run()
