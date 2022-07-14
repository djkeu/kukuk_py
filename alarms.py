from re import I
import time
from datetime import datetime

from kivy.core.audio import SoundLoader


def kuku_once():
    """Play kuku sound once."""
    kuku_sound = 'sounds/keukuk03.wav'

    sound = SoundLoader.load(kuku_sound)
    time.sleep(1)
    sound.play()
 

def kuku_times(times):
    """Play kuku sound multiple times in a row."""
    for i in range(0, times):
        kuku_once()


def quarterly_alarms():
    """Play kuku sound every 15 minutes."""
    alarms = ("15:00", "30:00", "45:00")
    current_time = datetime.now().strftime("%M:%S")

    if current_time in alarms:
        kuku_once()


def hourly_alarms():
    """Play kuku sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")

    for i in range(1, 25):
        if i < 13:
            times = i
        else:
            times = (i - 12)

        hour = f"{i:02}"
        if current_time == f"{hour}:00:00":
            kuku_times(times)


def minutely_alarms():
    """ Play kuku sound according to the minutes."""
    current_time = datetime.now().strftime("%M:%S")
    intervals = (00, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55)

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
        
        minute = f"{i:01}"
        if current_time == f"{minute}:00":
            kuku_times(times)


    """
    for i in intervals:
        times = 1
        seconds = f"{i:02}"

        if current_time == f"{seconds}":
            kuku_times(times)
    """