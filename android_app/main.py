from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

relays = [{'nr': 1, 'start': '18:00', 'end': '20:00', 'weekdays': ['Mo']},
          {'nr': 2, 'start': '16:00', 'end': '18:00', 'weekdays': ['Tu', 'Th']},
          {'nr': 3, 'start': '18:00', 'end': '20:00', 'weekdays': ['Tu', 'Fr']},
         ]
# relays = []

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
    self.weekday_button = Button(text=weekdays)
    self.add_widget(self.weekday_button)

    # Create checkbox/radio button to trigger manual override
    self.manual_checkbox = CheckBox()

    manual_layout = BoxLayout()
    manual_layout.add_widget(self.manual_checkbox)
    self.add_widget(manual_layout)
    # manual_layout
    # self.add_widget(self.manual_checkbox)

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

  def __init__(self, **kwargs):
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

class SettingsPopupContent(GridLayout):

  def __init__(self, **kwargs):
    super(SettingsPopupContent, self).__init__(**kwargs)
    self.rows = 3

    self.add_widget(Label(text='User Name'))
    self.username = TextInput(multiline=False)
    self.add_widget(self.username)

    self.add_widget(Label(text='Password'))
    self.password = TextInput(password=True, multiline=False)
    self.add_widget(self.password)

    self.add_widget(Label(text=''))
    self.button_login = Button(text='Log in')
    self.add_widget(self.button_login)

class SettingsPopupLayout(AnchorLayout):

  def __init__(self, **kwargs):
    super(SettingsPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)
    settings_popup_content = SettingsPopupContent()
    self.popup = Popup(title='Settings',
                       content=settings_popup_content,
                       size_hint=(None, None),
                       size=(Window.width*0.9, Window.height*0.25),
                      )

class RootScreen(GridLayout):

  def __init__(self, **kwargs):
    super(RootScreen, self).__init__(**kwargs)
    # self.orientation = 'vertical'
    # self.spacing = [0, 0]
    # self.padding = [0, 0]
    self.rows = 3
    popup_layout = SettingsPopupLayout()
    self.settings_button = Button(text='>',
                                  size_hint=(None, None),
                                  width=int(Window.height)/12.,
                                  height=int(Window.height)/12.,
                                  on_release=popup_layout.popup.open
                                 )
    self.add_widget(self.settings_button)

    relay_controler_layout = RelayControlersLayout(orientation='tb-lr')
    self.add_widget(relay_controler_layout)

class WateringControlSystemApp(App):
  def build(self):
    # return Button(text='Something')
    # return Label(text='Hello world')
    return RootScreen()

WateringControlSystemApp().run()
