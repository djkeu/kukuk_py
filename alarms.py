# from os import times
import time
from datetime import datetime

from playsound import playsound


def play_kuku_sound():
    """Play kuku sound once."""
    kuku_sound = 'sounds/keukuk03.wav'

    time.sleep(0.3)
    playsound(kuku_sound)


def times_kuku(times):
    """Play kuku sound multiple times in a row."""
    for i in range(0, times):
        play_kuku_sound()


def quarterly_alarms():
    """Play kuku sound every 15 minutes."""
    alarms = ["15:00", "30:00", "45:00"]
    current_time = datetime.now().strftime("%M:%S")

    if current_time in alarms:
        play_kuku_sound()


def hourly_alarms():
    """Play kuku sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")

    hours = range(1, 25)

    for i in hours:
        if i < 13:
            times = i
        else:
            times = (i - 12)

        hour = f"{i:02}"

        if current_time == f"{hour}:00:00":
            times_kuku(times)


def minutely_alarms():
    """Sound alarm every ten seconds for testing purposes."""
    current_time = datetime.now().strftime("%S")
    intervals = (00, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55)

    for i in intervals:
        times = 2
        seconds = f"{i:02}"

        if current_time == f"{seconds}":
            times_kuku(times)
