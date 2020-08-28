from typing import Callable, List, Optional

from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch

import widgets.state
from widgets.share import WEEKDAYS_MAPPING

class WeekdaySwitch(Switch):

  def __init__(self, relay_nr: int, weekday: str, **kwargs):
    super(WeekdaySwitch, self).__init__(**kwargs)
    self.relay_nr = relay_nr
    self.weekday = weekday

def update_relays_state(instance, value):

  relay_to_modify = [relay
                     for relay in widgets.state.relays
                     if relay['nr'] == instance.relay_nr
                    ][0]

  if value:
    relay_to_modify['weekdays'].append(WEEKDAYS_MAPPING[instance.weekday])
  else:
    relay_to_modify['weekdays'].remove(WEEKDAYS_MAPPING[instance.weekday])
  relay_to_modify['weekdays'].sort()

  for idx, relay in enumerate(widgets.state.relays):
    if relay['nr'] == instance.relay_nr:
      widgets.state.relays[idx] = relay_to_modify

class WeekdaysPopupContent(GridLayout):

  def __init__(self, relay_nr: int, weekdays: List[int], **kwargs):
    super(WeekdaysPopupContent, self).__init__(**kwargs)
    self.columns = 2
    self.rows = 7

    self.weekday_switches = {}

    for weekday in WEEKDAYS_MAPPING.keys():
      self.add_widget(Label(text=weekday))

      if WEEKDAYS_MAPPING[weekday] in weekdays:
        active = True
      else:
        active = False

      weekday_switch = WeekdaySwitch(relay_nr, weekday, active=active)
      weekday_switch.bind(active=update_relays_state)

      self.weekday_switches[weekday] = weekday_switch
      self.add_widget(self.weekday_switches[weekday])

class WeekdaysPopupLayout(AnchorLayout):

  def __init__(self,
               relay_nr: int,
               weekdays: List[int],
               **kwargs
              ):
    super(WeekdaysPopupLayout, self).__init__(anchor_x='right', anchor_y='bottom', **kwargs)
    weekdays_popup_content = WeekdaysPopupContent(relay_nr, weekdays)
    self.popup = Popup(title='Select weekdays',
                       content=weekdays_popup_content,
                       size_hint=(None, None),
                       size=(Window.width*0.9, Window.height*0.45),
                      )
