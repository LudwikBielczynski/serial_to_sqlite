from typing import Any, Dict

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

import widgets.state
from widgets.weedays_popup import WeekdaysPopupLayout

class TopLabels(BoxLayout):

  def __init__(self, **kwargs):
    super(TopLabels, self).__init__(**kwargs)
    self.orientation = 'horizontal'
    self.cols = 5
    self.height = 0.1
    self.add_widget(Label(text='Section'))
    self.add_widget(Label(text='Start'))
    self.add_widget(Label(text='End'))
    self.add_widget(Label(text='Weekday'))
    self.add_widget(Label(text='Manual'))

class WeekdaysButton(Button):

  def __init__(self, relay: Dict[str, Any], **kwargs):
    self.relay = relay
    super(WeekdaysButton, self).__init__(text=self.create_text_label(),
                                         **kwargs)

  def create_text_label(self):
    weekdays_text = ''
    for weekday in self.relay['weekdays']:
      weekdays_text += f'{weekday},'
    return weekdays_text[:-1]

  def update(self, relay: Dict[str, Any]):
    self.relay = relay
    self.text = self.create_text_label()

class RelayControlerWidget(GridLayout):

  def __init__(self, relay: Dict[str, Any], **kwargs):
    super(RelayControlerWidget, self).__init__(**kwargs)
    self.cols = 5
    self.relay = relay
    self.generate_widgets()

  def generate_widgets(self) -> None:
    self.label = Label(text=f'Relay {self.relay["nr"]}')

    def validate_time_input(time_str):
      '''Checks if the string representing time is well formed'''
      is_valid = True
      hours = int(time_str.split(':')[0])
      if (hours >= 24) | (hours < 0):
          is_valid = False

      minutes = int(time_str.split(':')[1])
      if (minutes >= 60) | (minutes < 0):
          is_valid = False
      return is_valid


    def time_start_on_enter(instance):
      is_valid = validate_time_input(instance.text)
      if is_valid:
        for relay_nr, relay in enumerate(widgets.state.relays):
          if relay['nr'] == self.relay['nr']:
            widgets.state.relays[relay_nr]['start'] = instance.text

    self.time_start = TextInput(text=self.relay['start'],
                                multiline=False,
                                halign='center',
                                on_text_validate=time_start_on_enter,
                               )

    def time_end_on_enter(instance):
      is_valid = validate_time_input(instance.text)
      if is_valid:
        for relay_nr, relay in enumerate(widgets.state.relays):
          if relay['nr'] == self.relay['nr']:
            widgets.state.relays[relay_nr]['end'] = instance.text

    self.time_end = TextInput(text=self.relay['end'],
                              multiline=False,
                              halign='center',
                              on_text_validate=time_end_on_enter,
                             )
    self.weekdays_layout = WeekdaysPopupLayout(self.relay['nr'], self.relay['weekdays'])
    self.weekday_button = WeekdaysButton(self.relay,
                                         on_release=self.weekdays_layout.popup.open,
                                        )
    self.manual_checkbox = CheckBox()

    self.add_widget(self.label)
    self.add_widget(self.time_start)
    self.add_widget(self.time_end)
    self.add_widget(self.weekday_button)
    self.add_widget(self.manual_checkbox)

  def update_weekday_button_text(self, relay: Dict[str, Any]):
    self.weekday_button.update(relay)

class RelayControlersLayout(StackLayout):

  def __init__(self, **kwargs):
    super(RelayControlersLayout, self).__init__(**kwargs)
    self.add_widget(TopLabels(size_hint=(1, 0.06), spacing=(0, 0),))
    self.relays_control_widgets = []

    self.create_relay_controler_widgets()

  def create_relay_controler_widgets(self):
    for relay in widgets.state.relays:
      relay_controler_widget = RelayControlerWidget(relay,
                                                    size_hint=(1, 0.06),
                                                    spacing=(0, 0),
                                                   )
      self.relays_control_widgets.append(relay_controler_widget)
      self.add_widget(relay_controler_widget)

    self.update_view_button = Button(text='Update view',
                                     size_hint=(None, None),
                                     width=Window.width,
                                     height=int(Window.height)/12.,
                                     on_release=self.update_relay_buttons,
                                    )
    self.add_widget(self.update_view_button)

  def remove_relay_controler_widgets(self):
    for relay_controler_widget in self.relays_control_widgets:
      self.remove_widget(relay_controler_widget)
    self.remove_widget(self.update_view_button)

  def update_relay_buttons(self, instance):
    self.remove_relay_controler_widgets()
    self.create_relay_controler_widgets()
