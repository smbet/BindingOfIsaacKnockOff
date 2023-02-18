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
BULLET_SPEED = 700

BULLET_COOLDOWN = FPS // 5  # shoots X times per sec in 'FPS // X
bullet_shot_at  = 0         # tracks when bullet is shot in terms of ticks
bullet_shotQ    = False     # tracks to see if a bullet was shot (so you can't spam in multiple directions)

# all_of_the_bullets will store each bullet as a list of length 2 in the format:
#          all_of_the_bullets = [ [bullet_rect_object, "bullet_direction"] ]
# example: all_of_the_bullets = [ [bullet_rect, "E"], [bullet_rect, "NW"], [bullet_rect, "SE"], [bullet_rect, "S"] ]
all_of_the_bullets = []

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
    bullet_shotQ = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            the_game_is_running = False
        # if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
                # all_of_the_bullets.append([
                #                            pygame.Rect(player_pos[0], player_pos[1], 15, 15),
                #                            "N"
                #                            ])

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
    

    if total_num_of_ticks > (bullet_shot_at + BULLET_COOLDOWN):
        if pressed_keys[pygame.K_UP] and not bullet_shotQ:
            all_of_the_bullets.append([
                                    #    pygame.Rect(player_pos[0], player_pos[1], 15, 15),
                                    pygame.Rect(
                                                player_pos[0] + pygame.Surface.get_width(player)  / 2, 
                                                player_pos[1] + pygame.Surface.get_height(player) / 2, 
                                                15, 15),
                                    "N"
                                    ])
            bullet_shot_at = total_num_of_ticks
            bullet_shotQ   = True
        if pressed_keys[pygame.K_DOWN] and not bullet_shotQ:
            all_of_the_bullets.append([
                                    #    pygame.Rect(player_pos[0], player_pos[1], 15, 15),
                                    pygame.Rect(
                                                player_pos[0] + pygame.Surface.get_width(player)  / 2, 
                                                player_pos[1] + pygame.Surface.get_height(player) / 2, 
                                                15, 15),
                                    "S"
                                    ])
            bullet_shot_at = total_num_of_ticks
            bullet_shotQ   = True
        if pressed_keys[pygame.K_RIGHT] and not bullet_shotQ:
            all_of_the_bullets.append([
                                    #    pygame.Rect(player_pos[0], player_pos[1], 15, 15),
                                    pygame.Rect(
                                                player_pos[0] + pygame.Surface.get_width(player)  / 2, 
                                                player_pos[1] + pygame.Surface.get_height(player) / 2, 
                                                15, 15),
                                    "E"
                                    ])
            bullet_shot_at = total_num_of_ticks
            bullet_shotQ   = True
        if pressed_keys[pygame.K_LEFT] and not bullet_shotQ:
            all_of_the_bullets.append([
                                    #    pygame.Rect(player_pos[0], player_pos[1], 15, 15),
                                    pygame.Rect(
                                                player_pos[0] + pygame.Surface.get_width(player)  / 2, 
                                                player_pos[1] + pygame.Surface.get_height(player) / 2, 
                                                15, 15),
                                    "W"
                                    ])
            bullet_shot_at = total_num_of_ticks
            bullet_shotQ   = True


    screen.fill(BLACK)
    screen.blit(player, player_pos)

    for this_bullet in all_of_the_bullets:
        if (this_bullet[0].centerx <= 0) or (this_bullet[0].centerx >= WIDTH) or (this_bullet[0].centery <= 0) or (this_bullet[0].centery >= HEIGHT):
            all_of_the_bullets.remove(this_bullet)
    
    for i in range(len(all_of_the_bullets)):
        if all_of_the_bullets[i][1] == "N":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], 0, -BULLET_SPEED / dt)
        if all_of_the_bullets[i][1] == "S":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], 0, BULLET_SPEED / dt)
        if all_of_the_bullets[i][1] == "E":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], BULLET_SPEED / dt, 0)
        if all_of_the_bullets[i][1] == "W":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], -BULLET_SPEED / dt, 0)
        pygame.draw.rect(screen, RED, all_of_the_bullets[i][0])
    
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