"""
Created on Thu Feb 16 08:16:11 2023

Authors:
- Joshua Maldonado
  joshuamaldonado4432@gmail.com
- Another Name
  TheirEmail@email.net

"""

# testing change

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
PLAYER_SPEED = 500
BULLET_SPEED = 5

all_of_the_bullets = []
bullets_N  = []
bullets_NW = []
bullets_W  = []
bullets_SW = []
bullets_S  = []
bullets_SE = []
bullets_E  = []
bullets_NE = []


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


player      = pygame.image.load("resources/small_moon.png").convert()
player_rect = player.get_rect()
player_pos  = list( player_rect.center )

bullet      = pygame.image.load("resources/tictac_20x20.png").convert()


# bullets = []
# def shoot():
#     bullet      = pygame.image.load("resources/tictac_20x20.png").convert()   # THIS IS SUPPOSED TO GIVE A SURFACE BUT IT'S GIVING ME A RECT :((((((
#     bullet_rect = bullet.get_rect(center = player_pos)
#     bullet_pos  = player_pos
#     bullets.append([bullet_rect, bullet_pos])

total_num_of_ticks  = 0
the_game_is_running = True
while the_game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            the_game_is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bullets_E.append(
                                #   bullet.get_rect(center = player_pos), 
                                  pygame.Rect(player_pos[0], player_pos[1], 15, 15)
                                #   [player_pos[0], player_pos[1]]  # assigned like this instead of 'player_pos' to 'untie' variables
                                  )
                all_of_the_bullets.append( bullets_E[-1] )
    
    

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]:
        the_game_is_running = False

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
        
    # if pressed_keys[pygame.K_LSHIFT] or pressed_keys[pygame.K_RSHIFT]:
    #     # shoot()
    #     bullet      = pygame.image.load("resources/tictac_20x20.png").convert()   # THIS IS SUPPOSED TO GIVE A SURFACE BUT IT'S GIVING ME A RECT :((((((
    #     bullet_rect = bullet.get_rect(center = player_pos)
    #     bullet_pos  = player_pos
    #     bullets.append([bullet_rect, bullet_pos])



    screen.fill(BLACK)
    screen.blit(player, player_pos)

    for this_bullet in all_of_the_bullets:
        if (this_bullet.centerx <= 0) or (this_bullet.centerx >= WIDTH) or (this_bullet.centery <= 0) or (this_bullet.centery >= HEIGHT):
            this_bullet.remove
    
    for e in range(len(bullets_E)):
        bullets_E[e] = pygame.Rect.move(bullets_E[e], BULLET_SPEED, 0)
        pygame.draw.rect(screen, RED, bullets_E[e])
    
    pygame.display.update()
    if (total_num_of_ticks % 10 == 0):
        print("player pos = ("+ str(
                                    round(player_pos[0], 4)
                                    )+", "+str(
                                            round(player_pos[1], 4)
                                            ) +")")
        print("number of bullets: "+ str(len(all_of_the_bullets)))

    pygame.time.delay(1000//FPS)
    total_num_of_ticks += 1
#
print("done")