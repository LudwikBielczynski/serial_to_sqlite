from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

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

class RelayControlersLayout(StackLayout):

  def __init__(self, relays, **kwargs):
    super(RelayControlersLayout, self).__init__(**kwargs)
    self.add_widget(TopLabels(size_hint=(1, 0.06), spacing=(0, 0),))
    self.relays_control_widgets = []
    for relay in relays:
      relay_controler_widget = RelayControlerWidget(relay,
                                                    size_hint=(1, 0.06),
                                                    spacing=(0, 0),
                                                   )
      self.relays_control_widgets.append(relay_controler_widget)
      self.add_widget(relay_controler_widget)

class RelayControlerWidget(GridLayout):

  def __init__(self, relay, **kwargs):
    super(RelayControlerWidget, self).__init__(**kwargs)
    self.cols = 5

    self.add_widget(Label(text=f'Relay {relay["nr"]}'))

    self.time_start = TextInput(text=relay['start'], multiline=False, halign='center')
    self.add_widget(self.time_start)

    self.time_end = TextInput(text=relay['end'], multiline=False, halign='center')
    self.add_widget(self.time_end)

    weekdays = ''
    for weekday in relay['weekdays']:
      weekdays += f'{weekday}, '

    weekdays = weekdays[:-2]
    weekdays_layout = WeekdaysPopupLayout()
    self.weekday_button = Button(text=weekdays,
                                 on_release=weekdays_layout.popup.open
                                )

    self.add_widget(self.weekday_button)

    # Create checkbox/radio button to trigger manual override
    self.manual_checkbox = CheckBox()

    manual_layout = BoxLayout()
    manual_layout.add_widget(self.manual_checkbox)
    self.add_widget(manual_layout)
    # manual_layout
    # self.add_widget(self.manual_checkbox)
