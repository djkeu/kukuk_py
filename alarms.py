import time
from datetime import datetime

from kivy.core.audio import SoundLoader


def kuku_once():
    """ Play kuku sound once. """
    kuku_sound = 'sounds/keukuk03.wav'

    sound = SoundLoader.load(kuku_sound)
    sound.play()
 

def quarterly_alarms():
    """Play kuku sound every 15 minutes."""
    current_quarterly_time = datetime.now().strftime("%M:%S.%f")[: -5]

    alarms = (
        "15:00.1", 
        "30:00.1", 
        "45:00.1"
        )

    if current_quarterly_time in alarms:
        kuku_once()
        print(f"Alarm sounded at: {current_quarterly_time}")


def test_quarterly_alarms():
    """Play kuku sound every 15 minutes."""
    current_secondly_time = datetime.now().strftime("%S.%f")[: -5]
    alarms = ("06.2", "16.2", "26.2", "36.2", "46.2", "56.2")

    if current_secondly_time in alarms:
        kuku_once()
        print(current_secondly_time)


def kuku_times(times):
    """ Play kuku sound multiple times in a row. """
    for i in range(0, times):
        kuku_once()
        time.sleep(1.1)


def hourly_alarms():
    """ Play kuku sound according to the hours. """
    current_hourly_time = datetime.now().strftime("%H:%M:%S")

    for i in range(1, 25):
        if i < 13:
            times = i
        else:
            times = (i - 12)

        hour = f"{i:02}:00:00"
        if current_hourly_time == hour:
            kuku_times(times)


def test_hourly_alarms():
    """ Play kuku sound according to the minutes. """
    # For testing purposes only
    current_minutely_time = datetime.now().strftime("%M:%S")

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
        if current_minutely_time == minute:
            print(f"Minute: {minute}")
            print(f"Current time: {current_minutely_time}")
            print(f"Times:  {times}")
            kuku_times(times)
