from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from widgets.weedays_popup import WeekdaysPopupLayout
from widgets.relay_controler import RelayControlersLayout
from widgets.settings_popup import SettingsPopupLayout
import widgets.state

class RootScreen(GridLayout):

  def __init__(self, **kwargs):
    super(RootScreen, self).__init__(**kwargs)
    self.rows = 3

    popup_layout = SettingsPopupLayout()
    self.settings_button = Button(text='>',
                                  size_hint=(None, None),
                                  width=int(Window.height)/12.,
                                  height=int(Window.height)/12.,
                                  on_release=popup_layout.popup.open
                                 )
    self.add_widget(self.settings_button)

    # self.update_button = Button(text='Update',
    #                             width=int(Window.height)/12.,
    #                             height=int(Window.height)/50.,)
    # self.add_widget(self.update_button)

    relay_controler_layout = RelayControlersLayout(orientation='tb-lr')
    self.add_widget(relay_controler_layout)

class WateringControlSystemApp(App):

  def build(self):
    # Load relays state
    widgets.state.relays = [
      {'nr': 1, 'start': '18:00', 'end': '20:00', 'weekdays': [1]},
      {'nr': 2, 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
      {'nr': 3, 'start': '18:00', 'end': '20:00', 'weekdays': [2, 4, 6]},
      {'nr': 4, 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
      ]
    return RootScreen()

WateringControlSystemApp().run()
