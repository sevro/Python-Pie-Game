# Draws one thousand random lines

import sys
import random
import pygame
from   pygame.locals import *

# Setup
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("One THOUSAND lines")
myfont = pygame.font.Font(None,60)

class Point():
    """ A simple point class """
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toTuple(self):
        return (self.x,self.y)

    def toString(self):
        return "{X:" + str(self.x) + ",Y:" + str(self.y) + "}"


# Main
lines = 0
screen.fill((0,0,0))
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    
    if lines < 1000:
        color = [0,0,0]
        # Generate & set a random color for the line
        for shade in range (3):
            color[shade] = random.randint(0,255)
        
        # Randomize line width
        width = random.randint(1,5)

        # Generate random line points
        p1 = Point(random.randint(0,600), random.randint(0,500))
        p2 = Point(random.randint(0,600), random.randint(0,500))

        # Draw line
        pygame.draw.line(screen, color, p1.toTuple(), p2.toTuple(), width)

        pygame.display.update()
        lines += 1
