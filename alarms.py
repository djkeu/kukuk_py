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
    times = 0
    mins_secs = ":00:00"


    # use range() ?
    # test.py


    if current_time == f"01{mins_secs}" or current_time == f"13{mins_secs}":
        times = 1
    elif current_time == f"02{mins_secs}" or current_time == f"14{mins_secs}":
        times = 2
    elif current_time == f"03{mins_secs}" or current_time == f"15{mins_secs}":
        times = 3
    elif current_time == f"04{mins_secs}" or current_time == f"16{mins_secs}":
        times = 4
    elif current_time == f"05{mins_secs}" or current_time == f"17{mins_secs}":
        times = 5
    elif current_time == f"06{mins_secs}" or current_time == f"18{mins_secs}":
        times = 6
    elif current_time == f"07{mins_secs}" or current_time == f"19{mins_secs}":
        times = 7
    elif current_time == f"08{mins_secs}" or current_time == f"20{mins_secs}":
        times = 8
    elif current_time == f"09{mins_secs}" or current_time == f"21{mins_secs}":
        times = 9
    elif current_time == f"10{mins_secs}" or current_time == f"22{mins_secs}":
        times = 10
    elif current_time == f"11{mins_secs}" or current_time == f"23{mins_secs}":
        times = 11
    elif current_time == f"12{mins_secs}" or current_time == f"00{mins_secs}":
        times = 12

    times_kuku(times)


def hourly_alarms_test():
    """Play kuku sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")
    times = 0
    mins_secs = ":00:00"


def hourly_alarms():
    """Play kuku sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")
    times = 0
    mins_secs = ":00:00"


    # use range() ?
    # test.py


    if current_time == f"01{mins_secs}" or current_time == f"13{mins_secs}":
        times = 1
    elif current_time == f"02{mins_secs}" or current_time == f"14{mins_secs}":
        times = 2
    elif current_time == f"03{mins_secs}" or current_time == f"15{mins_secs}":
        times = 3
    elif current_time == f"04{mins_secs}" or current_time == f"16{mins_secs}":
        times = 4
    elif current_time == f"05{mins_secs}" or current_time == f"17{mins_secs}":
        times = 5
    elif current_time == f"06{mins_secs}" or current_time == f"18{mins_secs}":
        times = 6
    elif current_time == f"07{mins_secs}" or current_time == f"19{mins_secs}":
        times = 7
    elif current_time == f"08{mins_secs}" or current_time == f"20{mins_secs}":
        times = 8
    elif current_time == f"09{mins_secs}" or current_time == f"21{mins_secs}":
        times = 9
    elif current_time == f"10{mins_secs}" or current_time == f"22{mins_secs}":
        times = 10
    elif current_time == f"11{mins_secs}" or current_time == f"23{mins_secs}":
        times = 11
    elif current_time == f"12{mins_secs}" or current_time == f"00{mins_secs}":
        times = 12

    times_kuku(times)


def hourly_alarms():
    """Play kuku sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")
    times = 0
    mins_secs = ":00:00"

    pm_times = range(1, 13)
    am_times = range(13, 25)

    for i in pm_times:
        hour = f"{i:02}"
        print(f"{hour}{mins_secs} - {times}")
        if current_time == f"{hour}{mins_secs}":
            times +=1

    for i in am_times:
        hour = f"{i:02}"
        print(f"{hour}{mins_secs} - {times}")
        if current_time == f"{hour}{mins_secs}":
            times +=1


    times_kuku(times)
