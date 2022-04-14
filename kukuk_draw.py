import pygame
from settings import Settings


def draw_lines():
    """Draw stuff with pygame.draw."""
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(settings.window_size)
    first_color = settings.first_color

    size = (200, 200)
    points = [(125, 0), (50, 125), (25, 150), (0, 125)]

    lines = pygame.Surface(size)
    pygame.draw.lines(lines, first_color, False, points)

    lines_closed = pygame.Surface(size)
    pygame.draw.lines(lines_closed, first_color, True, points)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    
        screen.blit(lines, (125, 125))
        screen.blit(lines_closed, (125, 125))
        pygame.display.update()

draw_lines()
