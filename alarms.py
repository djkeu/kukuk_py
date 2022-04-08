from datetime import datetime
import time
from playsound import playsound

def minutely():
    """Make kukuk sound every 15 seconds, for testing purposes."""
    minutely_alarms = ["00", "30", "15", "45"]
    current_time = datetime.now().strftime("%S")

    if current_time in minutely_alarms:
        time.sleep(1)
        playsound('sounds/keukuk04.wav')
        
def quarterly():
    """Make kukuk sound every 15 minutes."""
    quarterly_alarms = ["00:00", "15:00", "30:00", "45:00"]
    current_time = datetime.now().strftime("%M:%S")

    if current_time in quarterly_alarms:
        time.sleep(1)
        playsound('sounds/keukuk04.wav')
