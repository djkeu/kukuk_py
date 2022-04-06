# Program to mimic a cuckoo-clock
import pygame

from settings import Settings


class Kukuk:
    """Class to control behaviour of the cuckoo's clock."""

    def __init__(self) -> None:
        """Initialize clock."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.window_size)
        pygame.display.set_caption(self.settings.window_caption)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def run_clock(self):
        """Start the loop for the clock."""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update_screen()


# Create and call instance of Kukuk()
if __name__ == '__main__':
    ku = Kukuk()
    ku.run_clock()
