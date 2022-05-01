__version__ = "0.1.2"

import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from datetime import datetime
from alarms import quarterly_alarms, hourly_alarms


class BoxLayoutKukuk(BoxLayout):
    pass


class Klok(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.now = datetime.now()
        self.my_label.text = self.now.strftime("%H:%M:%M")


class KukukApp(App):
    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
    event = Clock.schedule_interval(alarms_callback, 1 / 30)


if __name__ == '__main__':
    KukukApp().run()
