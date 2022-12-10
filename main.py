__version__ = "0.1.6"

import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from time import strftime

from alarms import hourly_alarms 
from alarms import quarterly_alarms 


Window.size=(500, 400)

class BoxLayoutKukuk(BoxLayout):
    pass


class KukukApp(App):
    def update_time(self, i_val):
        self.root.ids.kuku_time.text = strftime("%H:%M:%S")

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def alarms_callback(dt):
        hourly_alarms()
        quarterly_alarms()
    
    event = Clock.schedule_interval(alarms_callback, 1 / 11)


if __name__ == '__main__':
    KukukApp().run()
