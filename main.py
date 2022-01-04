import pygame
from pygame.locals import *

pygame.init()

WIDTH = 640
HEIGHT = 480

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

FPS = 60

timer = pygame.time.Clock()

running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

while running:

    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
