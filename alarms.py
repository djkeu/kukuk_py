from datetime import datetime
from playsound import playsound

def quarterly():
    """Make kukuk to go off every 15 minutes."""
    quarterly_alarms = ["52:00", "15:00", "30:00", "45:00"]
    current_time = datetime.now().strftime("%M:%S")

    if current_time in quarterly_alarms:
        playsound('sounds/keukuk04.wav')
        

quarterly()
