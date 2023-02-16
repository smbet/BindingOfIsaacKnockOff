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
import math
import pygame
from pygame.locals import *



pygame.init()

# define pygame things and essential global things
SIZE = WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode(SIZE)

FPS = 30
clock = pygame.time.Clock()
dt = clock.tick(FPS)

SPEED_CORRECTION = 1 / math.sqrt(2)
PLAYER_SPEED = 120
BULLET_SPEED = 1000


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


player = pygame.image.load("small_moon.png")
player_rect = player.get_rect()
player_pos  = list( player_rect.center )

the_game_is_running = True
while the_game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            the_game_is_running = False
        if event.type == pygame.KEYDOWN:
            print("keydown")
    
    

    pressed_keys = pygame.key.get_pressed()

    # start jank
    correct_speed = False
    if (pressed_keys[pygame.K_w] and pressed_keys[pygame.K_a]) or (pressed_keys[pygame.K_w] and pressed_keys[pygame.K_d]) or (pressed_keys[pygame.K_s] and pressed_keys[pygame.K_a]) or (pressed_keys[pygame.K_s] and pressed_keys[pygame.K_d]):
        correct_speed = True
    # end jank
    if pressed_keys[pygame.K_w]:
        if correct_speed:
            player_pos[1] -= SPEED_CORRECTION * PLAYER_SPEED / dt
        else:
            player_pos[1] -= PLAYER_SPEED / dt
    if pressed_keys[pygame.K_s]:
        if correct_speed:
            player_pos[1] += SPEED_CORRECTION * PLAYER_SPEED / dt
        else:
            player_pos[1] += PLAYER_SPEED / dt
    if pressed_keys[pygame.K_a]:
        if correct_speed:
            player_pos[0] -= SPEED_CORRECTION * PLAYER_SPEED / dt
        else:
            player_pos[0] -= PLAYER_SPEED / dt
    if pressed_keys[pygame.K_d]:
        if correct_speed:
            player_pos[0] += SPEED_CORRECTION * PLAYER_SPEED / dt
        else:
            player_pos[0] += PLAYER_SPEED / dt


    screen.fill(BLACK)
    screen.blit(player, player_pos)
    pygame.display.update()
    print("player pos = ("+ str(
                                round(player_pos[0], 4)
                                )+", "+str(
                                           round(player_pos[1], 4)
                                           ) +")")

    pygame.time.delay(1000//FPS)
#
print("done")