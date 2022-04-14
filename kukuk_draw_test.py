import pygame

def draw_lines(self):
    """Draw stuff with pygame.draw."""
    self.size = (200, 200)
    self.points = [(125, 0), (50, 125), (25, 150), (0, 125)]

    self.lines = pygame.Surface(self.size)
    pygame.draw.lines(self.lines, self.first_color, False, self.points)

    self.lines_closed = pygame.Surface(self.size)
    pygame.draw.lines(self.lines_closed, self.first_color, True, self.points)


