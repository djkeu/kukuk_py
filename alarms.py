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
            print(f"Hourly alarms are alright!!\n")


def quarterly_alarms():
    """Play kuku sound every 15 minutes."""
    current_quarterly_time = datetime.now().strftime("%M:%S")
    current_logged_time = datetime.now().strftime("%H:%M:%S")

    alarms = ("15:00", "30:00", "45:00")

    if current_quarterly_time in alarms:
        kuku_once()
        time.sleep(1)
        print(f"Q-alarm sounded at: {current_logged_time}")
        
        if current_quarterly_time == "45:00":
            print(f"Q-alarms are alright!!\n")


def minutely_alarms():
    """ 
    Play kuku sound according to the minutes. 
    For testing purposes only.
    """
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
            multiple_kukus(times)
