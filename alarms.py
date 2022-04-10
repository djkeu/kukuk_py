import time
from datetime import datetime

from playsound import playsound
from settings import Settings


def play_kuku_sound():
    """Play the kuku sound once."""
    settings = Settings()
    time.sleep(0.5)
    playsound(settings.kuku_sound)


def minutely_alarms():
    """Make kukuk sound every 5 seconds, for testing purposes."""
    alarms = ["00", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
    current_time = datetime.now().strftime("%S")

    if current_time in alarms:
        play_kuku_sound()
        

def quarterly_alarms():
    """Make kukuk sound every 15 minutes."""
    alarms = ["15:00", "30:00", "45:00"]
    current_time = datetime.now().strftime("%M:%S")

    if current_time in alarms:
        play_kuku_sound()

def hourly_alarms():
    """Make kukuk sound according to the hours."""
    alarms = ["00:00:00", "01:00:00", "02:00:00",
            "03:00:00", "04:00:00", "05:00:00",
            "06:00:00", "07:00:00", "08:00:00",
            "09:00:00", "10:00:00", "11:00:00",
            "12:00:00", "13:00:00", "14:00:00",
            "15:00:00", "16:00:00", "17:00:00",
            "18:00:00", "19:00:00", "20:00:00",
            "21:00:00", "22:00:00", "23:00:00",
    ]
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time in alarms:
        play_kuku_sound()
