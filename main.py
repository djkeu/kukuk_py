__version__ = "0.1.3"

import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from time import strftime
from alarms import quarterly_alarms, hourly_alarms


class BoxLayoutKukuk(BoxLayout):
    pass


class KukukApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = strftime("%H:%M:%S")

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
    
    event = Clock.schedule_interval(alarms_callback, 1 / 30)


if __name__ == '__main__':
    KukukApp().run()
