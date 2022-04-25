import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window

from alarms import quarterly_alarms, hourly_alarms


class BoxLayoutKukuk(BoxLayout):
    pass


class Klok(Button):
    pass

    """Model the cuckoo's clock."""

    """
    text = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
    text += "\n\n\n\t\t\t   kukuk   \t\t\t"
    text += "\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
    """

    """
    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
    event = Clock.schedule_interval(alarms_callback, 1 / 30)
    """


class KukukApp(App):
   
    def build(self):
        """
        red = 61
        green = 43
        blue = 31
        
        bg_color = (red/255.0, green/255.0, blue/255.0, 1)
        Window.clearcolor = bg_color
        """
        
    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
    event = Clock.schedule_interval(alarms_callback, 1 / 30)
        
    
if __name__ == '__main__':
    KukukApp().run()
