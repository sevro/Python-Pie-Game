# Floating rectangle

import sys
import random
import pygame
from pygame.locals import *

# Setup
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Floating Rectangle")


def randColor(color):
    for shade in range(3):
        color[shade] = random.randint(0,255)


# Vars
width = 0
vel_x = random.choice((-2,-1,1,2))
vel_y = random.choice((-2,-1,1,2))
pos_x = 20
pos_y = 20
color = [0,0,0]
randColor(color)


# Main
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))

    # Move the rectangle
    pos_x += vel_x
    pos_y += vel_y

    # Check edges
    if pos_x >= 500:
        vel_x = random.choice((-2,-1))
        randColor(color)
    elif pos_x <= 0:
        vel_x = random.choice((1,2))
        randColor(color)
    if pos_y >= 400:
        vel_y = random.choice((-2,-1))
        randColor(color)
    elif pos_y <= 0:
        vel_y = random.choice((1,2))
        randColor(color)

    pos = pos_x, pos_y, 100, 100

    pygame.draw.rect(screen, color, pos, width)
    pygame.display.update()
