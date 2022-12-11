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
from alarms import minutely_alarms


Window.size=(500, 400)

class BoxLayoutKukuk(BoxLayout):
    """" Add docstring """
    pass


class KukukApp(App):
    """" Add docstring """

    def update_time(self, i_val):
        """" Add docstring """
        self.root.ids.kuku_time.text = strftime("%H:%M:%S")

    def on_start(self):
        """" Add docstring """
        Clock.schedule_interval(self.update_time, 1)

    def alarms_callback(dt):
        """" Add docstring """
        # quarterly_alarms()
        # hourly_alarms()
        minutely_alarms()

        
    
    event = Clock.schedule_interval(alarms_callback, 1 / 11)


if __name__ == '__main__':
    KukukApp().run()
