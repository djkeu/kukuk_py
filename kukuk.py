import pygame
from playsound import playsound
from datetime import datetime
import time

from settings import Settings
from alarms import quarterly


class Kukuk:
    """Class to control behaviour of the cuckoo's clock."""

    def __init__(self) -> None:
        """Initialize clock."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.window_size)
        pygame.display.set_caption(self.settings.window_caption)

        self.kuku_sound = self.settings.kuku_sound

    def update_screen(self):
        """Update screen, flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def run_clock(self):
        """Start the loop for the clock."""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        playsound('sounds/keukuk04.wav')

            quarterly_alarms = ["00", "15", "30", "45", "15:00", "30:00", "45:00"]
            current_time = datetime.now().strftime("%S")

            if current_time in quarterly_alarms:
                time.sleep(1)
                playsound('sounds/keukuk04.wav')

            self.update_screen()


if __name__ == '__main__':
    ku = Kukuk()
    ku.run_clock()
