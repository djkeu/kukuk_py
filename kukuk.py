import pygame

from settings import Settings
from alarms import quarterly_alarms, hourly_alarms


class Kukuk:
    """Class to control behaviour of the cuckoo's clock."""

    def __init__(self) -> None:
        """Initialize clock."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.window_size)
        pygame.display.set_caption(self.settings.window_caption)
        self.first_color = self.settings.first_color

    def draw_lines(self):
        """Draw stuff with pygame.draw."""
        self.size = (500, 500)

        self.line = pygame.Surface(self.size)
        pygame.draw.line(self.line, self.first_color, (0, 0), (500, 500))  # Start at topleft and ends at bottomright.
    
    def update_screen(self):
        """Update screen, flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.draw_lines()


        pygame.display.flip()

    def run_clock(self):
        """Start the loop for the clock."""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            quarterly_alarms()
            hourly_alarms()

            self.update_screen()


if __name__ == '__main__':
    ku = Kukuk()
    ku.run_clock()
