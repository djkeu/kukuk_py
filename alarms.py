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


def hourly_alarms_bak2():
    """Play kuku sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")
    # times = 0  # Probably abundant, awaiting refactoring
    mins_secs = ":00:00"

    pm_hours = range(1, 13)
    am_hours = range(13, 25)

    for i in pm_hours:
        hour = f"{i:02}"

        if current_time == f"{hour}{mins_secs}":
            times = i
            times_kuku(times)

    for i in am_hours:
        hour = f"{i:02}"
        if current_time == f"{hour}{mins_secs}":
            times = (i - 12)

            times_kuku(times)

def hourly_alarms():
    """Play kuku sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")
    mins_secs = ":00:00"

    hours = range(1, 25)

    for i in hours:
        if i < 13:
            times = i
        else:
            times = (i - 12)

        hour = f"{i:02}"

        if current_time == f"{hour}{mins_secs}":
            times_kuku(times)
