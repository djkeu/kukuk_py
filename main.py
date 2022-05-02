__version__ = "0.1.3"

import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from datetime import datetime
from alarms import quarterly_alarms, hourly_alarms


class BoxLayoutKukuk(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        klok_text = f"Kukuk is gestart om {current_time}"
        
        klok = Label(text=klok_text, size_hint=(1, .2))
        self.add_widget(klok)


class KukukApp(App):
    def klok_callback(dt):
        BoxLayoutKukuk()

    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
    
    event = Clock.schedule_interval(klok_callback, 1 / 30)
    event = Clock.schedule_interval(alarms_callback, 1 / 30)


if __name__ == '__main__':
    KukukApp().run()
