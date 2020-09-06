from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from widgets.weedays_popup import WeekdaysPopupLayout
from widgets.relay_controler import RelayControlersLayout
from widgets.settings_popup import SettingsPopupLayout
import widgets.state

# TODO: Implement multi screen layout
# https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html

# TODO: Implement manual turning on and off

class RootScreen(GridLayout):

  def __init__(self, **kwargs):
    super(RootScreen, self).__init__(**kwargs)
    self.rows = 3

    self.popup_layout = SettingsPopupLayout()
    self.settings_button = Button(text='>',
                                  size_hint=(None, None),
                                  width=int(Window.height)/12.,
                                  height=int(Window.height)/12.,
                                  on_release=self.popup_layout.popup.open
                                 )
    self.add_widget(self.settings_button)

    self.relay_controler_layout = RelayControlersLayout(orientation='tb-lr')
    self.add_widget(self.relay_controler_layout)

class WateringControlSystemApp(App):

  def build(self):
    root = RootScreen()
    return root

WateringControlSystemApp().run()
