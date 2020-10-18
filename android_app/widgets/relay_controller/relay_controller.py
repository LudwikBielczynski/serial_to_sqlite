from typing import Any, Dict

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
import requests

import widgets.state
from widgets.info_bubble import print_on_info_bubble
from widgets.watering_scheduler_communicator import WateringSchedulerCommunicator

Builder.load_file('widgets/relay_controller/top_labels.kv')
class TopLabels(BoxLayout):
    pass

Builder.load_file('widgets/relay_controller/relay_controller_button.kv')
class RelayControllerButton(BoxLayout, Button):
    def __init__(self, relay, **kwargs):
        self.relay = relay

        super(RelayControllerButton, self).__init__(**kwargs)

    @property
    def label(self):
        return f'{self.relay["section_name"]} ({self.relay["channel"]})'

    @property
    def weekdays(self):
        weekdays_text = ''
        for weekday in self.relay['weekdays']:
            weekdays_text += f'{weekday}'
        return weekdays_text

    def update_view(self):
        self.relay_button_label.text = self.label
        self.relay_button_start.text = self.relay['start']
        self.relay_button_end.text = self.relay['end']
        self.relay_button_weekdays.text = self.weekdays

class RelayControllerWidget(BoxLayout):

    def __init__(self, relay: Dict[str, Any], **kwargs):
        super(RelayControllerWidget, self).__init__(**kwargs)
        orientation = 'horizontal'

        self.relay = relay
        self.relay_controller_button = RelayControllerButton(self.relay)
        self.add_widget(self.relay_controller_button)

class RelayControllersLayout(StackLayout):

    def __init__(self, **kwargs):
        super(RelayControllersLayout, self).__init__(**kwargs)

        self.communicator = WateringSchedulerCommunicator(widgets.state.host)

    @property
    def relays_control_widget_names(self):
        return [attr
                for attr in dir(self)
                if 'relays_control_widget_' in attr
                if attr != 'relays_control_widget_names'
               ]

    def create_relay_controller_widgets(self):
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
                    RelayControllerWidget(relay, size_hint=(1, 0.06), spacing=(0, 0))
                   )
            self.add_widget(getattr(self, relay_widget_name))

    def update_relay_widgets(self, *args):
        # Never remove widgets, as it leads to a shit-storm with weak references on which handling
        # kivy is not transparent. On Linux - no problems, on android... no comment.
        if len(self.relays_control_widget_names) == 0:
            self.create_relay_controller_widgets()

        else:
            # Get widget for which the modification was done
            for relays_control_widget_name in self.relays_control_widget_names:
                widget = getattr(self, relays_control_widget_name)
                if widget.relay['channel'] == widgets.state.relay['channel']:
                    widget.children[0].relay = widgets.state.relay
                    widget.children[0].update_view()

            # Check if state was changed
            relays_state_current = self.get_widgets_current_state()

            def flatten(relays):
                return ['_'.join([str(value) for value in relay.values()])
                        for relay in relays_state_current
                       ]
            relays_state_current_flat = set(flatten(relays_state_current))
            relays_state_flat = set(flatten(widgets.state.relays))

            if relays_state_current_flat != relays_state_flat:
                print('unsynchronized')
                relay_diff = ((relays_state_current_flat - relays_state_flat) |
                              (relays_state_current_flat - relays_state_flat))
                print(relay_diff)

    def remove_widgets(self):
        for relays_control_widget_name in self.relays_control_widget_names:
            widget = getattr(self, relays_control_widget_name)
            self.remove_widget(widget)
            delattr(self, relays_control_widget_name)

    def get_widgets_current_state(self):
        relays_state_current = []
        for relays_control_widget_name in self.relays_control_widget_names:
            widget = getattr(self, relays_control_widget_name)
            relays_state_current.append(widget.children[0].relay)

        return relays_state_current

    def delete_all_schedule(self, *args):
        self.communicator.delete_all_schedule(widgets.state.relays)

        widgets.state.relays = self.communicator.format_relays_data()
        self.update_relay_widgets(None)

    def send_schedule_to_host(self, *args):
        self.communicator.delete_all_schedule(widgets.state.relays)
        self.communicator.send_all_schedule_to_host(widgets.state.relays)
