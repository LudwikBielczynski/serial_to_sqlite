import calendar
from typing import List

from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch

class WeekdaysPopupContent(GridLayout):

# FIXME: Popup appears only for the first and last relay

  def __init__(self, weekdays: List[str], **kwargs):
    super(WeekdaysPopupContent, self).__init__(**kwargs)
    self.columns = 2
    self.rows = 7

    self.weekday_switches = {}
    weekdays_mapping = {weekday_name: nr + 1
                        for nr, weekday_name in enumerate(calendar.day_name)}

    for weekday in weekdays_mapping.keys():
      self.add_widget(Label(text=weekday))

      if str(weekdays_mapping[weekday]) in weekdays:
        active = True
      else:
        active = False

      self.weekday_switches[weekday] = Switch(active=active)
      self.add_widget(self.weekday_switches[weekday])

class WeekdaysPopupLayout(AnchorLayout):

  def __init__(self, weekdays: List[str], **kwargs):
    super(WeekdaysPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)
    weekdays_popup_content = WeekdaysPopupContent(weekdays)
    self.popup = Popup(title='Select weekdays',
                       content=weekdays_popup_content,
                       size_hint=(None, None),
                       size=(Window.width*0.9, Window.height*0.45),
                      )
