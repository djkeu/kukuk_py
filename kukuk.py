# Program to mimic a cuckoo-clock
import pygame

from settings import Settings

class Kukuk:
    """Class to control behaviour of the cuckoo's clock."""

    def __init__(self) -> None:
        """Initialize clock."""
        pygame.init()
        self.window_size = (400, 300)
        self.window_caption = "Kukuk"
        self.bg_color = (123, 234, 222)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_caption)

    def run_clock(self):
        """Start the loop for the clock."""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    ku = Kukuk()
    ku.run_clock()