__version__ = "0.1.2"

import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from alarms import minutely_alarms, quarterly_alarms, hourly_alarms


class BoxLayoutKukuk(BoxLayout):
    pass


class KukukApp(App):
   
    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
        minutely_alarms()
    event = Clock.schedule_interval(alarms_callback, 1 / 10)


if __name__ == '__main__':
    KukukApp().run()
