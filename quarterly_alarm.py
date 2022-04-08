from datetime import datetime
from playsound import playsound

def quarterly():
    """Make kukuk to go off every 15 minutes."""
    while True:
        quarterly_alarms = ["21", "15", "30", "45"]
        current_time = datetime.now().strftime("%M")
        if current_time in quarterly_alarms:
            playsound('sounds/keukuk04.wav')
            return False

quarterly()
