# Bomb Catcher Game
# Chapter 4

import sys, random, time, pygame, math
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def boom():
    seconds = 1
    clock_start = time.clock()
    current = time.clock() - clock_start
    print_text(font2, 225, 250, "BOOM!")
    pygame.display.update()
    while seconds >= current:
        current = time.clock() - clock_start

def rand_red():
    """ Generates random shades from (bright) red to yellow """
    shade1 = random.randint(125,255)
    shade2 = random.randint(0,255)
    shade3 = 0
    if shade1 < shade2:
        shade1 = 255
    return (shade1, shade2, shade3)

def choose_lr(bomb_x):
    """ Chooses to move the bomb left or right """
    if bomb_x > 100 and bomb_x < 500:
        return random.choice((True,False))
    elif bomb_x < 100:
        return False
    else:
        return True


    

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bomb Catching Game")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 50)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0
miss = False

lives = 3
score = 0
clock_start = 0
game_over = True
mouse_x = mouse_y = 0

pos_x = 300
pos_y = 460

bomb_x = random.randint(0,500)
bomb_y = -50
vel_y = 0.7
vel_x = 0.1
left = choose_lr(bomb_x) # decides if vel_x is + or -

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,0,100))

    if game_over:
        print_text(font1, 100, 200, "<CLICK TO PLAY>") 
    else:
        #move the bomb
        bomb_y += vel_y
        if left:
            bomb_x += -vel_x
        else:
            bomb_x += vel_x

        #has the player missed the bomb?
        if bomb_y > 500:
            miss = True
            bomb_x = random.randint(0, 500)
            left = choose_lr(bomb_x) # decides if vel_x is + or -
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True

        #see if player has caught the bomb
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 10
                bomb_x = random.randint(0, 500)
                left =  choose_lr(bomb_x) # decides if vel_x is + or -
                bomb_y = -50
        
        #draw the bomb
        pygame.draw.circle(screen, black, (int(bomb_x-4),int(bomb_y)-4), 30, 0)
        pygame.draw.circle(screen, yellow, (int(bomb_x),int(bomb_y)), 30, 0)

        #draw bomb fuse
        color       = rand_red()
        width       = 3
        start_angle = 0
        stop_angle  = math.pi/2
        Rect        = ((bomb_x-72,bomb_y-70), (75,75))
        pygame.draw.arc(screen, color, Rect, start_angle, stop_angle, width)

        #set basket position
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
        #draw basket
        pygame.draw.rect(screen, black, (pos_x-4,pos_y-4,120,40), 0)
        pygame.draw.rect(screen, red, (pos_x,pos_y,120,40), 0)

    #print # of lives
    print_text(font1, 0, 0, "LIVES: " + str(lives))

    #print score
    print_text(font1, 500, 0, "SCORE: " + str(score))
    
    if miss == True:
        boom()
        miss = False
    else:
        pygame.display.update()
