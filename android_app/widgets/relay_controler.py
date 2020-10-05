from typing import Any, Dict

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
import requests

import widgets.state
from widgets.info_bubble import print_on_info_bubble
from widgets.watering_scheduler_communicator import WateringSchedulerCommunicator
from widgets.weedays_popup import WeekdaysPopupLayout

Builder.load_file('widgets/top_labels.kv')
class TopLabels(BoxLayout):
    pass

Builder.load_file('widgets/relay_controller_button.kv')
class RelayControllerButton(BoxLayout, Button):
    def __init__(self, relay, **kwargs):
        self.relay = relay
        self.label = f'{self.relay["section_name"]} ({self.relay["channel"]})'
        self.weekdays = self.create_weekdays_text_label()

        super(RelayControllerButton, self).__init__(**kwargs)

    def create_weekdays_text_label(self):
        weekdays_text = ''
        for weekday in self.relay['weekdays']:
            weekdays_text += f'{weekday}'
        return weekdays_text

class RelayControlerWidget(BoxLayout):

    def __init__(self, relay: Dict[str, Any], **kwargs):
        super(RelayControlerWidget, self).__init__(**kwargs)
        orientation = 'horizontal'

        self.relay = relay
        self.relay_controller_button = RelayControllerButton(self.relay)
        self.add_widget(self.relay_controller_button)

class RelayControlersLayout(StackLayout):

    def __init__(self, **kwargs):
        super(RelayControlersLayout, self).__init__(**kwargs)
        self.relays_control_widgets = []

        # self.create_relay_controler_widgets()
        self.communicator = WateringSchedulerCommunicator(widgets.state.host)

    def create_relay_controler_widgets(self):
        if not hasattr(self, 'top_labels'):
            self.top_labels = TopLabels()
            self.add_widget(self.top_labels)

        button_settings = {
            'size_hint': (None, None),
            'width': Window.width,
            'height': int(Window.height)/15.,
        }

        for relay_nr, relay in enumerate(widgets.state.relays):
            relay_widget_name = f'relays_control_widget_{relay_nr}'
            setattr(self,
                    relay_widget_name,
                    RelayControlerWidget(relay, size_hint=(1, 0.06), spacing=(0, 0))
                   )
            self.add_widget(getattr(self, relay_widget_name))

    def update_relay_widgets(self, *args):
        # Never remove widgets, as it leads to a shitstorm with weak references on which handling
        # kivy is not transparent. On Linux - no problems, on android... no comment.
        self.create_relay_controler_widgets()
        # FIXME: Implement real update of the widgets created in create_relay_controler_widgets
        for relay_nr, relay in enumerate(widgets.state.relays):
            relay_widget_name = f'relays_control_widget_{relay_nr}'
            widget = getattr(self, relay_widget_name)

    def delete_all_schedule(self, *args):
        self.communicator.delete_all_schedule(widgets.state.relays)

        widgets.state.relays = self.communicator.get_formatted_relays_data()
        self.update_relay_widgets(None)

    def send_schedule_to_host(self, *args):
        self.communicator.delete_all_schedule(widgets.state.relays)
        self.communicator.send_all_schedule_to_host(widgets.state.relays)
