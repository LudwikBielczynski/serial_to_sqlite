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
from widgets.watering_scheduler_communicator import WateringSchedulerCommunicator
from widgets.weedays_popup import WeekdaysPopupLayout

Builder.load_file('widgets/top_labels.kv')

class TopLabels(BoxLayout):
    pass

class WeekdaysButton(Button):

    def __init__(self, relay: Dict[str, Any], **kwargs):
        self.relay = relay
        super(WeekdaysButton, self).__init__(text=self._create_text_label(),
                                            **kwargs)

    def _create_text_label(self):
        weekdays_text = ''
        for weekday in self.relay['weekdays']:
            weekdays_text += f'{weekday}'
        return weekdays_text

class RelayControlerWidget(GridLayout):

    def __init__(self, relay: Dict[str, Any], **kwargs):
        super(RelayControlerWidget, self).__init__(**kwargs)
        self.cols = 5
        self.relay = relay
        self._generate_widgets()

    def _generate_widgets(self) -> None:
        self.label = Label(text=f'{self.relay["section_name"]} ({self.relay["channel"]})')

        def validate_time_input(time_str):
            '''Checks if the string representing time is well formed'''
            is_valid = True
            hours = int(time_str.split(':')[0])
            if (hours >= 24) | (hours < 0):
                is_valid = False

            minutes = int(time_str.split(':')[1])
            if (minutes >= 60) | (minutes < 0):
                is_valid = False
            return is_valid

        def _time_start_on_enter(instance):
            is_valid = validate_time_input(instance.text)
            if is_valid:
                for relay_nr, relay in enumerate(widgets.state.relays):
                    if relay['channel'] == self.relay['channel']:
                        widgets.state.relays[relay_nr]['start'] = instance.text

        self.time_start = TextInput(text=self.relay['start'],
                                    multiline=False,
                                    halign='center',
                                    on_text_validate=_time_start_on_enter,
                                )

        def _time_end_on_enter(instance):
            is_valid = validate_time_input(instance.text)
            if is_valid:
                for relay_nr, relay in enumerate(widgets.state.relays):
                    if relay['channel'] == self.relay['channel']:
                        widgets.state.relays[relay_nr]['end'] = instance.text

        self.time_end = TextInput(text=self.relay['end'],
                                multiline=False,
                                halign='center',
                                on_text_validate=_time_end_on_enter,
                                )
        self.weekdays_layout = WeekdaysPopupLayout(self.relay['channel'], self.relay['weekdays'])
        self.weekday_button = WeekdaysButton(self.relay,
                                            on_release=self.weekdays_layout.popup.open,
                                            )
        self.manual_checkbox = CheckBox()

        self.add_widget(self.label)
        self.add_widget(self.time_start)
        self.add_widget(self.time_end)
        self.add_widget(self.weekday_button)
        self.add_widget(self.manual_checkbox)

class RelayControlersLayout(StackLayout):

    def __init__(self, **kwargs):
        super(RelayControlersLayout, self).__init__(**kwargs)
        self.relays_control_widgets = []

        self._create_relay_controler_widgets()

        self.communicator = WateringSchedulerCommunicator(widgets.state.host)

    def _create_relay_controler_widgets(self):
        button_settings = {
            'size_hint': (None, None),
            'width': Window.width,
            'height': int(Window.height)/15.,
        }

        self.update_view_button = Button(text='Update view', on_release=self.update_relay_widgets, **button_settings)
        self.add_widget(self.update_view_button)

        self.clear_all_button = Button(text='Clear all', on_release=self.delete_all_schedule, **button_settings)
        self.add_widget(self.clear_all_button)

        self.send_to_host_button = Button(text='Send to host', on_release=self.send_schedule_to_host, **button_settings)
        self.add_widget(self.send_to_host_button)

        self.logout_button = Button(text='Log out', on_release=self.logout, **button_settings)
        self.add_widget(self.logout_button)
        
        self.top_labels = TopLabels(size_hint=(1, 0.06), spacing=(0, 0),)
        self.add_widget(self.top_labels)
        for relay in widgets.state.relays:
            relay_controler_widget = RelayControlerWidget(relay,
                                                          size_hint=(1, 0.06),
                                                          spacing=(0, 0),
                                                        )
            self.relays_control_widgets.append(relay_controler_widget)
            self.add_widget(relay_controler_widget)

    def _remove_relay_controler_widgets(self):
        for relay_controler_widget in self.relays_control_widgets:
            self.remove_widget(relay_controler_widget)
        self.remove_widget(self.top_labels)
        self.remove_widget(self.update_view_button)
        self.remove_widget(self.clear_all_button)
        self.remove_widget(self.send_to_host_button)
        self.remove_widget(self.logout_button)

    def update_relay_widgets(self, *args):
        self._remove_relay_controler_widgets()
        self._create_relay_controler_widgets()

    def delete_all_schedule(self, instance):
        self.communicator.delete_all_schedule(widgets.state.relays)

        widgets.state.relays = self.communicator.get_formatted_relays_data()
        self.update_relay_widgets(None)

    def send_schedule_to_host(self, instance):
        self.communicator.delete_all_schedule(widgets.state.relays)
        self.communicator.send_all_schedule_to_host(widgets.state.relays)

    def logout(self, instance):
        widgets.state.relays = []
        widgets.state.username = ''
        widgets.state.password = ''
        
        manager = App.get_running_app().root
        manager.transition.direction = 'right'
        manager.current = 'login'
