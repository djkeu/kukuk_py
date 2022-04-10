import time
from datetime import datetime

from playsound import playsound
from settings import Settings


def play_kuku_sound():
    """Play kuku sound once."""
    settings = Settings()
    time.sleep(0.3)
    playsound(settings.kuku_sound)


def times_kuku(times):
    """Play kuku sound multiple times."""
    for i in range(0, times):
        play_kuku_sound()


def minutely_alarms_v1():
    """Play kuku sound every 5 seconds, for testing purposes."""
    alarms = ["00", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
    current_time = datetime.now().strftime("%S")

    if current_time in alarms:
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

    if current_time == "01:00:00" or current_time == "13:00:00":
        times = 1
        times_kuku(times)
    elif current_time == "02:00:00" or current_time == "14:00:00":
        times = 2
        times_kuku(times)
    elif current_time == "03:00:00" or current_time == "15:00:00":
        times = 3
        times_kuku(times)
    elif current_time == "04:00:00" or current_time == "16:00:00":
        times = 4
        times_kuku(times)
    elif current_time == "05:00:00" or current_time == "17:00:00":
        times = 5
        times_kuku(times)
    elif current_time == "06:00:00" or current_time == "18:00:00":
        times = 6
        times_kuku(times)
    elif current_time == "07:00:00" or current_time == "19:00:00":
        times = 7
        times_kuku(times)
    elif current_time == "08:00:00" or current_time == "20:00:00":
        times = 8
        times_kuku(times)
    elif current_time == "09:00:00" or current_time == "21:00:00":
        times = 9
        times_kuku(times)
    elif current_time == "10:00:00" or current_time == "22:00:00":
        times = 10
        times_kuku(times)
    elif current_time == "11:00:00" or current_time == "23:00:00":
        times = 11
        times_kuku(times)
    elif current_time == "12:00:00" or current_time == "00:00:00":
        times = 12
        times_kuku(times)


#def minutely_alarms_v2():
    """Play kuku sound every 10 seconds, for testing purposes."""
    #current_time = datetime.now().strftime("%S")
    """
    if current_time == "00":
        times = 1
        times_kuku(times)
    elif current_time == "10":
        times = 2
        print(times)
        times_kuku(times)
    elif current_time == "20":
        times = 3
        print(times)
        times_kuku(times)
    elif current_time == "30":
        times = 4
        print(times)
        times_kuku(times)
    elif current_time == "40":
        times = 5
        print(times)
        times_kuku(times)
    elif current_time == "50":
        times = 6
        print(times)
        times_kuku(times)
    """