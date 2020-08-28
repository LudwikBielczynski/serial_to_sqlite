from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

import widgets.state



def login(instance):
  # FIXME: Send HTTP request to host and unpack response
  print('logged in')
  widgets.state.relays = [
    {'nr': 1, 'start': '18:00', 'end': '20:00', 'weekdays': [1]},
    {'nr': 2, 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
    {'nr': 3, 'start': '18:00', 'end': '20:00', 'weekdays': [2, 4, 6]},
    {'nr': 4, 'start': '16:00', 'end': '18:00', 'weekdays': [2, 4]},
    ]

class SettingsPopupContent(GridLayout):

  def __init__(self, **kwargs):
    super(SettingsPopupContent, self).__init__(**kwargs)
    self.rows = 4

    self.add_widget(Label(text='Host'))
    self.host_input = TextInput(text=widgets.state.host, multiline=False)
    def on_host_input(instance, value):
      widgets.host = value
    self.host_input.bind(text=on_host_input)
    self.add_widget(self.host_input)

    self.add_widget(Label(text='User Name'))
    self.username_input = TextInput(text=widgets.state.username, multiline=False)
    def on_username_input(instance, value):
      widgets.username = value
    self.username_input.bind(text=on_username_input)
    self.add_widget(self.username_input)

    self.add_widget(Label(text='Password'))
    self.password_input = TextInput(text=widgets.state.password, password=True, multiline=False)
    def on_password_input(instance, value):
      widgets.password = value
    self.password_input.bind(text=on_password_input)
    self.add_widget(self.password_input)

    self.add_widget(Label(text=''))
    self.button_login = Button(text='Log in',
                               on_release=login
                              )
    self.add_widget(self.button_login)

class SettingsPopupLayout(AnchorLayout):

  def __init__(self, **kwargs):
    super(SettingsPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)
    settings_popup_content = SettingsPopupContent()
    self.popup = Popup(title='Settings',
                       content=settings_popup_content,
                       size_hint=(None, None),
                       size=(Window.width*0.9, Window.height*0.3),
                      )