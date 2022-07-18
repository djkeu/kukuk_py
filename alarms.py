import time
from datetime import datetime

from kivy.core.audio import SoundLoader


def kuku_once():
    """ Play kuku sound once. """
    kuku_sound = 'sounds/keukuk03.wav'

    sound = SoundLoader.load(kuku_sound)
    sound.play()
 

def quarterly_alarms():
    """Play kuku sound every 15 minutes."""
    alarms = (
        "15:00.1", 
        "30:00.1", 
        "45:00.1"
        )
    current_quarterly_time = datetime.now().strftime("%M:%S.%f")[: -5]

    if current_quarterly_time in alarms:
        kuku_once()


def test_quarterly_alarms_v2():
    """Play kuku sound every 15 minutes."""
    alarms = ("15:00", "30:00", "45:00")
    alarms = (
        "01:00.1", "02:00.1", "03:00.1", "04:00.1", "05:00.1",
        "06:00.1", "07:00.1", "08:00.1", "09:00.1", "10:00.1",
        "11:00.1", "12:00.1", "13:00.1", "14:00.1", "15:00.1",
        "16:00.1", "17:00.1", "18:00.1", "19:00.1", "20:00.1",
        "21:00.1", "22:00.1", "23:00.1", "24:00.1", "25:00.1",
        "26:00.1", "27:00.1", "28:00.1", "29:00.1", "30:00.1",
        "31:00.1", "32:00.1", "33:00.1", "34:00.1", "35:00.1",
        "36:00.1", "37:00.1", "38:00.1", "39:00.1", "40:00.1",
        "41:00.1", "42:00.1", "43:00.1", "44:00.1", "45:00.1",
        "46:00.1", "47:00.1", "48:00.1", "49:00.1", "50:00.1",
        "51:00.1", "52:00.1", "53:00.1", "54:00.1", "55:00.1",
        "56:00.1", "57:00.1", "58:00.1", "59:00.1"
        )
    current_quarterly_time = datetime.now().strftime("%M:%S.%f")[: -5]

    if current_quarterly_time in alarms:
        kuku_once()
        print(f"Alarm sounds at: {current_quarterly_time}")


def test_quarterly_alarms_v1():
    """Play kuku sound every 15 minutes."""
    current_secondly_time = datetime.now().strftime("%S.%f")[: -5]
    # print(current_secondly_time)
    alarms = ("06.2", "16.2", "26.2", "36.2", "46.2", "56.2")

    if current_secondly_time in alarms:
        kuku_once()
        print(current_secondly_time)
        # time.sleep(1)


def kuku_times(times):
    """ Play kuku sound multiple times in a row. """
    for i in range(0, times):
        kuku_once()
        time.sleep(1.1)


def hourly_alarms():
    """ Play kuku sound according to the hours. """
    current_hourly_time = datetime.now().strftime("%H:%M:%S")

    for i in range(1, 25):
        if i < 13:
            times = i
        else:
            times = (i - 12)

        hour = f"{i:02}:00:00"
        if current_hourly_time == hour:
            kuku_times(times)


def test_hourly_alarms():
    """ Play kuku sound according to the minutes. """
    # For testing purposes only
    current_minutely_time = datetime.now().strftime("%M:%S")

    for i in range(1, 60):
        if i < 11:
            times = i
        elif i < 21:
            times = i - 10
        elif i < 31:
            times = i - 20
        elif i < 41:
            times = i - 30
        elif i < 51:
            times = i - 40
        else:
            times = i - 50

        minute = f"{i:02}:00"
        if current_minutely_time == minute:
            print(f"Minute: {minute}")
            print(f"Current time: {current_minutely_time}")
            print(f"Times:  {times}")
            kuku_times(times)
