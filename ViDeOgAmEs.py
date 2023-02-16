"""
Created on Thu Feb 16 08:16:11 2023

Authors:
- Joshua Maldonado
  joshuamaldonado4432@gmail.com
- Another Name
  TheirEmail@email.net

"""


import time
import sys
import pygame
from pygame.locals import *



pygame.init()

# define pygame things and essential global things
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)

FPS = 30
clock = pygame.time.Clock()
dt = clock.tick(FPS)

PLAYER_SPEED = 1


# define lots of colors
BLACK   = (0,   0,   0)
GRAY    = (127, 127, 127)
WHITE   = (255, 255, 255)
RED     = (255, 0,   0)
GREEN   = (0,   255, 0)
BLUE    = (0,   0,   255)
YELLOW  = (255, 255, 0)
CYAN    = (0,   255, 255)
MAGENTA = (255, 0,   255)


ball = pygame.image.load("small_moon.png")
ballrect = ball.get_rect()


the_game_is_running = True
while the_game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            the_game_is_running = False
    

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_w]:
        ballrect = ballrect.move(
                                 [0, -PLAYER_SPEED]
                                 )
    if pressed_keys[pygame.K_a]:
        ballrect = ballrect.move(
                                 [-PLAYER_SPEED, 0]
                                 )
    if pressed_keys[pygame.K_s]:
        ballrect = ballrect.move(
                                 [0, PLAYER_SPEED]
                                 )
    if pressed_keys[pygame.K_d]:
        ballrect = ballrect.move(
                                 [PLAYER_SPEED, 0]
                                 )


    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.update()

print("done")