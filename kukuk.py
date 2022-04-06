# Program to mimic a cuckoo-clock
import pygame

window_size = (400, 300)
window_caption = "Kukuk"
bg_color = (123, 234, 222)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_caption)
screen.fill(bg_color)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
