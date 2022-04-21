from settings import Settings
from alarms import quarterly_alarms, hourly_alarms


class Kukuk:
    """Class to control behaviour of the cuckoo's clock."""

    def __init__(self) -> None:
        """Initialize clock."""
        self.settings = Settings()
        self.kuku_sound = 'sounds/keukuk03.wav'

    def run_clock(self):
        """Start the loop for the clock."""
        running = True

        while running:
            quarterly_alarms()
            hourly_alarms()


if __name__ == '__main__':
    ku = Kukuk()
    ku.run_clock()
