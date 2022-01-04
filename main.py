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


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.player = self.render()
        self.attacking = False
        self.tiro = None

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_RIGHT]:
            self.x += 0.5
        if keys_pressed[K_LEFT]:
            self.x -= 0.5
        if keys_pressed[K_UP]:
            self.attacking = True
            shoot = Shoot()
        if self.attacking:
            shoot.update()

    def render(self):
        medium_point = (self.x, self.y)
        left_point = (self.x - self.width / 2, self.y + self.height)
        right_point = (self.x + self.width / 2, self.y + self.height)
        triangle = pygame.draw.polygon(SCREEN, WHITE, (left_point, medium_point, right_point))
        return triangle


class Shoot:
    def __init__(self):
        self.radius = 5
        self.x = 0
        self.y = 0
        self.tiro = None

    def attack(self):
        initial_point = (player.x, player.y)
        self.y = player.y
        self.x = player.x
        self.tiro = pygame.draw.circle(SCREEN, WHITE, initial_point, 5)

    def update(self):
        self.y -= 1


player = Player(WIDTH / 2 - 25, HEIGHT - 50)

while running:

    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    player.update()
    player.render()

    pygame.display.flip()

pygame.quit()
