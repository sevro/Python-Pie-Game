# Draws an ellipse

import sys
import pygame
from pygame.locals import *
pygame.init()

# Setup
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Ellipse")
myfont = pygame.font.Font(None,60)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))

    # Draw the ellipse
    color = 255,255,0
    rect  = 125,125,350,200
    width = 6
    pygame.draw.ellipse(screen, color, rect, width)

    pygame.display.update()
