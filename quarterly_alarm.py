from datetime import datetime

def quarterly():
    """Make kukuk to go off every 15 minutes."""
    while True:
        quarterly_alarms = [00, 15, 30, 45, "00", "04", "05", "07", "10", "15", "30", "45"]
        current_time = datetime.now().strftime("%M")
        if current_time in quarterly_alarms:
            print("Weer een kwartier voorbij!")
            return False

# Test
quarterly()
