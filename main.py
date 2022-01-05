import pygame
from pygame.locals import *
from random import randint

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
RED = (255, 0, 0)
shoot_counter = 0


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
    def __init__(self, speed):
        self.y = None
        self.x = None
        self.center = (0, 0)
        self.radius = 10
        self.attacking = False
        self.shoot = None
        self.speed = speed

    def update(self):
        if self.attacking:
            self.y += self.speed

        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.attacking = False

    def render(self):
        if self.attacking:
            self.shoot = pygame.draw.circle(SCREEN, BLUE, (self.x, self.y), self.radius)

    def attack(self, center_x, center_y):
        self.attacking = True
        self.x = center_x
        self.y = center_y


class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = self.width
        self.invader = pygame.draw.rect(SCREEN, RED, (self.x, self.y, self.width, self.height))
        self.draw = True
        self.counter = 0
        self.speed = 0.1
        self.shoot = Shoot(speed=0.5)

    def render(self):
        if self.draw:
            self.invader = pygame.draw.rect(SCREEN, RED,  (self.x, self.y, self.width, self.height))

    def update(self):
        if self.shoot.attacking:
            self.shoot.update()
            self.shoot.render()
        for item in shoots:
            if self.invader.colliderect(item.shoot):
                self.draw = False
        if self.counter >= 0:
            self.x += self.speed
            if self.counter == 800:
                self.counter = -800
        elif self.counter < 0:
            self.x -= self.speed
        self.counter += 1
        # if True:
            # self.shoot.attack(self.x + self.width / 2, self.y + self.height)


shoots = []
invaders = []
for pos in range(0, HEIGHT - 20, 50):
    invaders.append(Invader(pos, 20))

while running:

    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_SPACE] and (shoot_counter > 360 or len(shoots) < 1):
        shoot = Shoot(speed=-0.5)
        shoots.append(shoot)
        shoot.attack(player.x, player.y)
        del shoot
        shoot_counter = 0
    player.update()
    player.render()
    for shoot in shoots:
        shoot.update()
        if shoot.y < 0:
            shoots.remove(shoot)
        shoot.render()
    for invader in invaders:
        invader.update()
        if not invader.draw:
            invaders.remove(invader)
        invader.render()
    if len(shoots) >= 1:
        shoot_counter += 1

    if len(invaders) < 1:
        for pos in range(0, HEIGHT - 20, 50):
            invaders.append(Invader(pos, 20))
    pygame.display.flip()

pygame.quit()
