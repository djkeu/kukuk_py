# Program to mimic a cuckoo-clock
import pygame

screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption("Kukuk")

bg_color = (123, 234, 222)
screen.fill(bg_color)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
