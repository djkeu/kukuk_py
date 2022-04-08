from datetime import datetime

def quarterly():
    """Make kukuk to go off every 15 minutes."""
    while True:
        quarterly_alarms = ["00", "04", "05", "07", "10", "17", "15", "30", "45"]
        current_time = datetime.now().strftime("%M")
        if current_time in quarterly_alarms:
            playsound('sounds/keukuk04.wav')
            return False

quarterly()
