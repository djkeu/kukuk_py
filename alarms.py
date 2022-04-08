from datetime import datetime
import time
from playsound import playsound

def minute_ly():
    """Make kukuk to go off every 15 minutes."""
    quarterly_alarms = ["00", "30", "15", "45"]
    current_time = datetime.now().strftime("%S")

    if current_time in quarterly_alarms:
        time.sleep(1)
        playsound('sounds/keukuk04.wav')
        
def quarterly():
    """Make kukuk to go off every 15 minutes."""
    quarterly_alarms = ["00:00", "15:00", "30:00", "45:00"]
    current_time = datetime.now().strftime("%M:%S")

    if current_time in quarterly_alarms:
        time.sleep(1)
        playsound('sounds/keukuk04.wav')
