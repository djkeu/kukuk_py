import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

from alarms import quarterly_alarms, hourly_alarms


class Kukuk(Label):
    """Class to control behaviour of the cuckoo's clock."""

    text = "Kukuk kukuk"
    text += "\n\n\t\t\t Kukuk \t\t\t"

    def alarms_callback(dt):
        quarterly_alarms()
        hourly_alarms()
    event = Clock.schedule_interval(alarms_callback, 1 / 30)


class KukukApp(App):

    def build(self):
        return Kukuk()


if __name__ == '__main__':
    KukukApp().run()
