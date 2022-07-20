import time
from datetime import datetime

from kivy.core.audio import SoundLoader


# Sound section
def kuku_once():
    """ Play kuku sound once. """
    kuku_sound_file = 'sounds/keukuk03.wav'

    kuku_sound = SoundLoader.load(kuku_sound_file)
    kuku_sound.play()
 

def multiple_kukus(times):
    """ Play kuku sound multiple times in a row. """
    for i in range(0, times):
        kuku_once()
        time.sleep(1.1)


# Alarms section
def quarterly_alarms():
    """Play kuku sound every 15 minutes."""
    current_quarterly_time = datetime.now().strftime("%M:%S.%f")[: -5]
    alarms = ("15:00.1", "30:00.1", "45:00.1")

    if current_quarterly_time in alarms:
        kuku_once()
        print(f"Alarm sounded at: {current_quarterly_time}")


def hourly_alarms():
    """ Play kuku sound according to the hours. """
    current_hourly_time = datetime.now().strftime("%H:%M:%S")

    for i in range(0, 24):
        if i == 0:
            times = 12
        elif i < 13:
            times = i
        else:
            times = (i - 12)

        hour = f"{i:02}:00:00"
        
        if hour == current_hourly_time:
            multiple_kukus(times)
            print(f"Hourly alarms sounded {times} times at: {current_hourly_time}")
