from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch

class WeekdaysPopupContent(GridLayout):

  def __init__(self, **kwargs):
    super(WeekdaysPopupContent, self).__init__(**kwargs)
    self.columns = 2
    self.rows = 7

    self.weekday_switches = {}
    for weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
      self.add_widget(Label(text=weekday))
      self.weekday_switches[weekday] = Switch()
      self.add_widget(self.weekday_switches[weekday])

class WeekdaysPopupLayout(AnchorLayout):

  def __init__(self, **kwargs):
    super(WeekdaysPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)
    weekdays_popup_content = WeekdaysPopupContent()
    self.popup = Popup(title='Select weekdays',
                       content=weekdays_popup_content,
                       size_hint=(None, None),
                       size=(Window.width*0.9, Window.height*0.45),
                      )
