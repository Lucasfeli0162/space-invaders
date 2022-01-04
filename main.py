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
BLUE = (0, 0, 255)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.player = self.render()
        self.attacking = False
        self.shoot = None
        self.shoot_y = None
        self.shoot_x = None
        self.speed = 0.2
        self.left_point = (self.x - self.width / 2, self.y + self.height)
        self.right_point = (self.x + self.width / 2, self.y + self.height)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RIGHT] and self.right_point[0] < WIDTH:
            self.x += self.speed
        if pressed_keys[K_LEFT] and self.left_point[0] > 0:
            self.x -= self.speed

    def render(self):
        medium_point = (self.x, self.y)
        self.left_point = (self.x - self.width / 2, self.y + self.height)
        self.right_point = (self.x + self.width / 2, self.y + self.height)
        triangle = pygame.draw.polygon(SCREEN, WHITE, (self.left_point, medium_point, self.right_point))
        return triangle


player = Player(WIDTH / 2 - 25, HEIGHT - 50)


class Shoot:
    def __init__(self):
        self.y = 100
        self.x = 100
        self.center = (0, 0)
        self.radius = 10
        self.attacking = False

    def update(self):
        if self.attacking:
            self.y -= 0.1

        if self.y - self.radius <= 0:
            self.attacking = False

    def render(self):
        if self.attacking:
            pygame.draw.circle(SCREEN, BLUE, (self.x, self.y), self.radius)

    def attack(self, center_x, center_y):
        self.attacking = True
        self.x = center_x
        self.y = center_y


shoot = Shoot()

while running:

    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_SPACE] and not shoot.attacking:
        shoot.attack(player.x, player.y)
    player.update()
    player.render()
    shoot.update()
    shoot.render()

    pygame.display.flip()

pygame.quit()
