import time
from datetime import datetime

from kivy.core.audio import SoundLoader


def kuku_once():
    """ Play kuku sound once. """
    kuku_sound = 'sounds/keukuk03.wav'

    sound = SoundLoader.load(kuku_sound)
    sound.play()
 

def quarterly_alarms():
    """ Play kuku sound every 15 minutes. """
    alarms = ("15:00", "30:00", "45:00")
    current_time = datetime.now().strftime("%M:%S")

    if current_time in alarms:
        kuku_once()


def test_quarterly_alarms():
    """ Play kuku sound every 15 minutes. """
    alarms = ("15:00", "30:00", "45:00")
    current_time = datetime.now().strftime("%M:%S")

    if current_time in alarms:
        kuku_once()


def kuku_times(times):
    """ Play kuku sound multiple times in a row. """
    for i in range(0, times):
        kuku_once()
        time.sleep(1.1)


def hourly_alarms():
    """ Play kuku sound according to the hours. """
    current_time = datetime.now().strftime("%H:%M:%S")

    for i in range(1, 25):
        if i < 13:
            times = i
        else:
            times = (i - 12)

        hour = f"{i:02}:00:00"
        if current_time == hour:
            kuku_times(times)


def test_hourly_alarms():
    """ Play kuku sound according to the minutes. """
    # For testing purposes only
    current_time = datetime.now().strftime("%M:%S")

    for i in range(1, 60):
        if i < 11:
            times = i
        elif i < 21:
            times = i - 10
        elif i < 31:
            times = i - 20
        elif i < 41:
            times = i - 30
        elif i < 51:
            times = i - 40
        else:
            times = i - 50

        minute = f"{i:02}:00"
        if current_time == minute:
            print(f"Minute: {minute}")
            print(f"Current time: {current_time}")
            print(f"Times:  {times}")
            kuku_times(times)
