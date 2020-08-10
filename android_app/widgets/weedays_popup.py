import calendar
from typing import List

from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch

import widgets.state

class WeekdaySwitch(Switch):

  def __init__(self, relay_nr: int, weekday: str, **kwargs):
    super(WeekdaySwitch, self).__init__(**kwargs)
    self.relay_nr = relay_nr
    self.weekday = weekday

class WeekdaysPopupContent(GridLayout):

# FIXME: Popup appears only for the first and last relay

  def __init__(self, relay_nr: int, weekdays: List[int], **kwargs):
    super(WeekdaysPopupContent, self).__init__(**kwargs)
    self.columns = 2
    self.rows = 7

    self.weekday_switches = {}
    weekdays_mapping = {weekday_name: nr + 1
                        for nr, weekday_name in enumerate(calendar.day_name)}

    def update_relays_state(instance, value):
      relay_to_modify = [relay
                         for relay in widgets.state.relays
                         if relay['nr'] == instance.relay_nr
                        ][0]

      if value:
        relay_to_modify['weekdays'].append(weekdays_mapping[instance.weekday])
      else:
        relay_to_modify['weekdays'].remove(weekdays_mapping[instance.weekday])
      relay_to_modify['weekdays'].sort()

      for idx, relay in enumerate(widgets.state.relays):
        if relay['nr'] == instance.relay_nr:
          widgets.state.relays[idx] = relay_to_modify

      print(widgets.state.relays)


    for weekday in weekdays_mapping.keys():
      self.add_widget(Label(text=weekday))

      if weekdays_mapping[weekday] in weekdays:
        active = True
      else:
        active = False

      weekday_switch = WeekdaySwitch(relay_nr, weekday, active=active)
      weekday_switch.bind(active=update_relays_state)

      self.weekday_switches[weekday] = weekday_switch
      self.add_widget(self.weekday_switches[weekday])

class WeekdaysPopupLayout(AnchorLayout):

  def __init__(self, relay_nr: int, weekdays: List[int], **kwargs):
    super(WeekdaysPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)
    weekdays_popup_content = WeekdaysPopupContent(relay_nr, weekdays)
    self.popup = Popup(title='Select weekdays',
                       content=weekdays_popup_content,
                       size_hint=(None, None),
                       size=(Window.width*0.9, Window.height*0.45),
                      )
