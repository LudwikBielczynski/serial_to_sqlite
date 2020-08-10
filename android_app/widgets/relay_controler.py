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

  def __init__(self, relay, **kwargs):
    self.relay = relay
    super(WeekdaysButton, self).__init__(text=self.create_text_label(),
                                         **kwargs)

  def create_text_label(self):
    weekdays_text = ''
    for weekday in self.relay['weekdays']:
      weekdays_text += f'{weekday},'
    return weekdays_text[:-1]

  def update(self):
    self.text = self.create_text_label()

class RelayControlerWidget(GridLayout):

  def __init__(self, relay, **kwargs):
    super(RelayControlerWidget, self).__init__(**kwargs)
    self.cols = 5

    self.add_widget(Label(text=f'Relay {relay["nr"]}'))

    self.time_start = TextInput(text=relay['start'], multiline=False, halign='center')
    self.add_widget(self.time_start)

    self.time_end = TextInput(text=relay['end'], multiline=False, halign='center')
    self.add_widget(self.time_end)

    # Create the weekday button with the selection popup
    weekdays_layout = WeekdaysPopupLayout(relay['nr'], relay['weekdays'])

    # weekdays_text = ''
    # for weekday in relay['weekdays']:
    #   weekdays_text += f'{weekday}, '

    self.weekday_button = WeekdaysButton(relay,
                                         on_release=weekdays_layout.popup.open,
                                        )

    self.add_widget(self.weekday_button)

    # Create checkbox/radio button to trigger manual override
    self.manual_checkbox = CheckBox()
    self.add_widget(self.manual_checkbox)

class RelayControlersLayout(StackLayout):

  def __init__(self, **kwargs):
    super(RelayControlersLayout, self).__init__(**kwargs)
    self.add_widget(TopLabels(size_hint=(1, 0.06), spacing=(0, 0),))
    self.relays_control_widgets = []
    for relay in widgets.state.relays:
      relay_controler_widget = RelayControlerWidget(relay,
                                                    size_hint=(1, 0.06),
                                                    spacing=(0, 0),
                                                   )
      self.relays_control_widgets.append(relay_controler_widget)
      self.add_widget(relay_controler_widget)
