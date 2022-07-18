__version__ = "0.1.4"

import kivy

kivy.require('2.1.0')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

from time import strftime
from alarms import quarterly_alarms 
from alarms import hourly_alarms
# from alarms import test_quarterly_alarms_v2
# from alarms import test_hourly_alarms


class BoxLayoutKukuk(BoxLayout):
    pass


class KukukApp(App):
    def update_time(self, i_val):
        self.root.ids.time.text = strftime("%H:%M:%S")

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
        # test_quarterly_alarms_v2()
        # test_hourly_alarms()
    
    event = Clock.schedule_interval(alarms_callback, 1 / 10)


if __name__ == '__main__':
    KukukApp().run()
