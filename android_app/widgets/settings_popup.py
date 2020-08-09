from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

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