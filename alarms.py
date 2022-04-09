import time
from datetime import datetime

from playsound import playsound
from settings import Settings


def play_kuku_sound():
    """Play the kuku sound once."""
    settings = Settings()
    time.sleep(1)
    playsound(settings.kuku_sound)


def minutely_alarms():
    """Make kukuk sound every 15 seconds, for testing purposes."""
    alarms = ["00", "30", "15", "45"]
    current_time = datetime.now().strftime("%S")

    if current_time in alarms:
        play_kuku_sound()
        

def quarterly_alarms():
    """Make kukuk sound every 15 minutes."""
    alarms = ["00:00", "15:00", "30:00", "45:00"]
    current_time = datetime.now().strftime("%M:%S")

    if current_time in alarms:
        play_kuku_sound()
