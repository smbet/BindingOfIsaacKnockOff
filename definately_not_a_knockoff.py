"""
Created on Thu Feb 16 08:16:11 2023

"""

# testing change

import time
import sys
import math
import numpy as np
import random
import pygame
from pygame.locals import *



pygame.init()
print("\n"*5)  # this is a spacer to make it easier to troubleshoot error messages

# define pygame things and essential global things
SIZE = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(SIZE)

TROUBLESHOOTING = False  # determines if print statements will occur after set amount of frames

FPS   = 30
clock = pygame.time.Clock()
dt    = clock.tick(FPS)

SPEED_CORRECTION      = 1 / math.sqrt(2)
PLAYER_SPEED          = 300
player_speed_variable = 0

BUBBLES_SPEED         = PLAYER_SPEED / 2
BUBBLES_COOLDOWN      = 0 # number of ticks that bubbles is immune after respawning

POWER_UP_FREQUENCY    = 5 * FPS
POWER_UP_INITIAL_WAIT = 2 * FPS
PLAYER_IMMUNITY_TIME  = 1 * FPS
POWER_UP_TYPES        = ["shield", "faster_shooting"]
all_of_the_power_ups  = []
# all_of_the_power_ups will store each bullet as a list of length 2 in the format:
#          all_of_the_power_ups = [ [power_up_rect_object, "power_up_type"] ]
# example: all_of_the_power_ups = [ [power_up_rect, "faster_shooting""], [power_up_rect, "extra_bullets"] ]

BULLET_SPEED          = 500
BULLET_SIZE           = 15        # x y height of box of bullet
BULLETS_PER_SECOND    = 5
bullet_boost          = 1
BULLET_COOLDOWN       = FPS // BULLETS_PER_SECOND
bullet_shot_at        = 0         # tracks when bullet is shot in terms of ticks
bullet_shotQ          = False     # tracks to see if a bullet was shot (so you can't spam in multiple directions)
def generate_bullet():
    return pygame.Rect(
                       player_pos[0] + pygame.Surface.get_width(player)  / 2, 
                       player_pos[1] + pygame.Surface.get_height(player) / 2, 
                       BULLET_SIZE, BULLET_SIZE
                       )
VALID_SHOT_DIRECTIONS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
all_of_the_bullets    = []
# all_of_the_bullets will store each bullet as a list of length 2 in the format:
#          all_of_the_bullets = [ [bullet_rect_object, "bullet_direction"] ]
# example: all_of_the_bullets = [ [bullet_rect, "E"], [bullet_rect, "NW"], [bullet_rect, "SE"], [bullet_rect, "S"] ]



player             = pygame.image.load("resources/moon_50x50.png").convert()
player_pos         = [WIDTH / 2, HEIGHT / 2]
PLAYER_WIDTH       = pygame.Surface.get_width(player)
PLAYER_HEIGHT      = pygame.Surface.get_height(player)
player_rectangle   = pygame.Rect(
                                 player_pos[0],
                                 player_pos[1],
                                 PLAYER_WIDTH,
                                 PLAYER_HEIGHT
                                 )


bubbles            = pygame.image.load("resources/Bubbles_50x50.png").convert()
bubbles_pos        = [WIDTH * random.random(), HEIGHT * random.random()]
BUBBLES_WIDTH      = pygame.Surface.get_width(bubbles)
BUBBLES_HEIGHT     = pygame.Surface.get_height(bubbles)
bubbles_rectangle  = pygame.Rect(
                                 bubbles_pos[0],
                                 bubbles_pos[1],
                                 BUBBLES_WIDTH,
                                 BUBBLES_HEIGHT
                                 )

power_up            = pygame.image.load("resources/shitty_arrow_40x40.png").convert()
bullet_speed_icon   = pygame.image.load("resources/bullet_speed_power_up_40x40.png").convert()
shield_icon         = pygame.image.load("resources/shield_power_up_40x40.png").convert()
POWER_UP_WIDTH      = pygame.Surface.get_width(bubbles)
POWER_UP_HEIGHT     = pygame.Surface.get_height(bubbles)
def generate_power_up():
    power_up_pos       = [WIDTH * random.random(), HEIGHT * random.random()]
    power_up_rectangle = pygame.Rect(
                                     power_up_pos[0],
                                     power_up_pos[1],
                                     POWER_UP_WIDTH,
                                     POWER_UP_HEIGHT
                                     )
    return power_up_rectangle


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



# initialize variables for loop
player_shields       = 0
previous_player_pos  = [player_pos[0] , player_pos[1] ]
previous_bubbles_pos = [bubbles_pos[0], bubbles_pos[1]]
bubbles_hit_tick     = 0
player_hit_tick      = 0
times_bubbles_killed = 0
total_num_of_ticks   = 0
the_game_is_running  = True
while the_game_is_running:
    bullet_shotQ = False
    player_out_of_bounds_x = False
    player_out_of_bounds_y = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            the_game_is_running = False

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]:
        the_game_is_running = False
    


    if total_num_of_ticks > (bubbles_hit_tick + BUBBLES_COOLDOWN):
        for b in all_of_the_bullets:
            if pygame.Rect.colliderect(bubbles_rectangle, b[0]):
                # print("bubbles it hit")
                respawnX = WIDTH  * random.random()
                respawnY = HEIGHT * random.random()
                # this should work, might need to fine tune the 
                radius = 4*pygame.Surface.get_width(player)
                while (np.sqrt( (respawnX - player_pos[0])**2 + (respawnY - player_pos[1])**2 ) < radius ):
                    respawnX = WIDTH  * random.random()
                    respawnY = HEIGHT * random.random()
                    # print("respawning bubbles")
                bubbles_pos[0] = respawnX
                bubbles_pos[1] = respawnY
                bubbles_hit_tick = total_num_of_ticks
                times_bubbles_killed += 1

                all_of_the_bullets.remove(b)

    if pygame.Rect.colliderect(bubbles_rectangle, player_rectangle) and (total_num_of_ticks > player_hit_tick + PLAYER_IMMUNITY_TIME):
        # print("you're getting hit!")
        if player_shields == 0:
            the_game_is_running = False
        else:
            player_shields -= 1
            player_hit_tick = total_num_of_ticks
        
        print("shields left: "+ str(player_shields))

    for this_power_up in all_of_the_power_ups:
        if pygame.Rect.colliderect(this_power_up[0], player_rectangle):
            if this_power_up[1] == "shield":
                player_shields += 1
                print("shields: "+ str(player_shields))
            if this_power_up[1] == "faster_shooting":
                bullet_boost += 1
                print("BULLET_BOOST ")
            if this_power_up[1] == "extra_bullets":
                print("extra_bullet not working yet")
            
            all_of_the_power_ups.remove(this_power_up)

    # player movement
    # start jank
    correct_speed = False
    if (pressed_keys[pygame.K_w] and pressed_keys[pygame.K_a]) or (pressed_keys[pygame.K_w] and pressed_keys[pygame.K_d]) or (pressed_keys[pygame.K_s] and pressed_keys[pygame.K_a]) or (pressed_keys[pygame.K_s] and pressed_keys[pygame.K_d]):
        correct_speed = True
    # end jank
    adjust_player_speed_by = (correct_speed * SPEED_CORRECTION + 1*(not correct_speed)) * PLAYER_SPEED // dt
    if (player_pos[0] < 0):
        player_out_of_bounds_x = True
        player_pos[0] = 1
    if (player_pos[0] > WIDTH - pygame.Surface.get_width(player)):
        player_out_of_bounds_x = True
        player_pos[0] = WIDTH - pygame.Surface.get_width(player) - 1
    if (player_pos[1] < 0):
        player_out_of_bounds_y = True
        player_pos[1] = 1
    if (player_pos[1] > HEIGHT - pygame.Surface.get_height(player)):
        player_out_of_bounds_y = True
        player_pos[1] = HEIGHT - pygame.Surface.get_height(player) - 1
    if pressed_keys[pygame.K_w]:
        player_pos[1] -= adjust_player_speed_by * (1 - player_out_of_bounds_y)
    if pressed_keys[pygame.K_s]:
        player_pos[1] += adjust_player_speed_by * (1 - player_out_of_bounds_y)
    if pressed_keys[pygame.K_a]:
        player_pos[0] -= adjust_player_speed_by * (1 - player_out_of_bounds_x)
    if pressed_keys[pygame.K_d]:
        player_pos[0] += adjust_player_speed_by * (1 - player_out_of_bounds_x)
    

    # bullet stuff
    if total_num_of_ticks > (bullet_shot_at + BULLET_COOLDOWN / bullet_boost):
        if (pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_RIGHT]) and not bullet_shotQ:
            direction    = "NE"
            bullet_shotQ = True
        if (pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_LEFT]) and not bullet_shotQ:
            direction    = "NW"
            bullet_shotQ = True
        if (pressed_keys[pygame.K_DOWN] and pressed_keys[pygame.K_RIGHT]) and not bullet_shotQ:
            direction    = "SE"
            bullet_shotQ = True
        if (pressed_keys[pygame.K_DOWN] and pressed_keys[pygame.K_LEFT]) and not bullet_shotQ:
            direction    = "SW"
            bullet_shotQ = True
        if pressed_keys[pygame.K_UP] and not bullet_shotQ:
            direction    = "N"
            bullet_shotQ = True
        if pressed_keys[pygame.K_DOWN] and not bullet_shotQ:
            direction    = "S"
            bullet_shotQ = True
        if pressed_keys[pygame.K_RIGHT] and not bullet_shotQ:
            direction    = "E"
            bullet_shotQ = True
        if pressed_keys[pygame.K_LEFT] and not bullet_shotQ:
            direction    = "W"
            bullet_shotQ = True
        if bullet_shotQ:
            bullet_shot_at = total_num_of_ticks
            all_of_the_bullets.append([generate_bullet(), direction])

    # stuff for bubbles
    # the "< 5" bit here was picked arbitrarily because it seemed to work to get rid of bubble's jitteryness
    if (abs(bubbles_pos[0] - player_pos[0]) < 5) and (abs(bubbles_pos[1] - player_pos[1]) < 5):
        bubbles_pos[0] = player_pos[0]
        bubbles_pos[1] = player_pos[1]
    else:
        adjust_bubbles_x = 0
        adjust_bubbles_y = 0
        if bubbles_pos[0] < player_pos[0] - pygame.Surface.get_height(player) / pygame.Surface.get_height(bubbles) :
            adjust_bubbles_x += BUBBLES_SPEED // dt
        if bubbles_pos[0] > player_pos[0] + pygame.Surface.get_height(player) / pygame.Surface.get_height(bubbles):
            adjust_bubbles_x -= BUBBLES_SPEED // dt
        if bubbles_pos[1] < player_pos[1] - pygame.Surface.get_width(player) /  pygame.Surface.get_width(bubbles):
            adjust_bubbles_y += BUBBLES_SPEED // dt
        if bubbles_pos[1] > player_pos[1] + pygame.Surface.get_width(player) /  pygame.Surface.get_width(bubbles):
            adjust_bubbles_y -= BUBBLES_SPEED // dt
        
        if (adjust_bubbles_x != 0) and (adjust_bubbles_y != 0):
            bubbles_pos[0] += SPEED_CORRECTION * adjust_bubbles_x // 1
            bubbles_pos[1] += SPEED_CORRECTION * adjust_bubbles_y // 1
        else:
            bubbles_pos[0] += adjust_bubbles_x
            bubbles_pos[1] += adjust_bubbles_y

    # power up stuff here
    if total_num_of_ticks > POWER_UP_INITIAL_WAIT:
        if (total_num_of_ticks % POWER_UP_FREQUENCY) == 0:
            generated_power_up = POWER_UP_TYPES[np.random.randint( len(POWER_UP_TYPES) )]
            all_of_the_power_ups.append([
                                         generate_power_up(),
                                         generated_power_up
                                         ])
            print("power_up = "+ str(generated_power_up))

    # try and fix player_rect and bubbles_rect here
    if previous_player_pos == player_pos:
        player_rectangle  = pygame.Rect.move(player_rectangle, 0, 0)
    else:
        player_rectangle  = pygame.Rect.move(
                                             player_rectangle, 
                                             (player_pos[0] - previous_player_pos[0]), 
                                             (player_pos[1] - previous_player_pos[1])
                                             )
    if previous_bubbles_pos == bubbles_pos:
        bubbles_rectangle = pygame.Rect.move(bubbles_rectangle, 0, 0)
    else:
        bubbles_rectangle = pygame.Rect.move(
                                             bubbles_rectangle, 
                                             bubbles_pos[0] - previous_bubbles_pos[0], 
                                             bubbles_pos[1] - previous_bubbles_pos[1])

    # screen stuff
    screen.fill(BLACK)
    screen.blit(player, player_pos)
    screen.blit(bubbles, bubbles_pos)
    for this_power_up in all_of_the_power_ups:
        if this_power_up[1] == "faster_shooting":
            screen.blit(bullet_speed_icon, 
                        [this_power_up[0].centerx, 
                        this_power_up[0].centery]
                        )
        if this_power_up[1] == "shield":
            screen.blit(shield_icon, 
                        [this_power_up[0].centerx, 
                        this_power_up[0].centery]
                        )
    
    # pygame.draw.rect(screen, BLUE,   player_rectangle )
    # pygame.draw.rect(screen, YELLOW, bubbles_rectangle)

    for this_bullet in all_of_the_bullets:
        if (this_bullet[0].centerx <= 0) or (this_bullet[0].centerx >= WIDTH) or (this_bullet[0].centery <= 0) or (this_bullet[0].centery >= HEIGHT):
            all_of_the_bullets.remove(this_bullet)


    
    for i in range(len(all_of_the_bullets)):
        if all_of_the_bullets[i][1] == "N":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], 0, -BULLET_SPEED / dt)
        if all_of_the_bullets[i][1] == "S":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], 0,  BULLET_SPEED / dt)
        if all_of_the_bullets[i][1] == "E":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0],  BULLET_SPEED / dt, 0)
        if all_of_the_bullets[i][1] == "W":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], -BULLET_SPEED / dt, 0)
        if all_of_the_bullets[i][1] == "NW":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], -SPEED_CORRECTION * BULLET_SPEED / dt, -SPEED_CORRECTION * BULLET_SPEED / dt)
        if all_of_the_bullets[i][1] == "NE":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0],  SPEED_CORRECTION * BULLET_SPEED / dt, -SPEED_CORRECTION * BULLET_SPEED / dt)
        if all_of_the_bullets[i][1] == "SW":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0], -SPEED_CORRECTION * BULLET_SPEED / dt,  SPEED_CORRECTION * BULLET_SPEED / dt)
        if all_of_the_bullets[i][1] == "SE":
            all_of_the_bullets[i][0] = pygame.Rect.move(all_of_the_bullets[i][0],  SPEED_CORRECTION * BULLET_SPEED / dt,  SPEED_CORRECTION * BULLET_SPEED / dt)
        
        pygame.draw.rect(screen, RED, all_of_the_bullets[i][0])
    
    pygame.display.update()

    if TROUBLESHOOTING:
        if (total_num_of_ticks % 5 == 0):
            print("player pos = ("+ str(
                                        round(player_pos[0], 4)
                                        )+", "+str(
                                                round(player_pos[1], 4)
                                                ) +")")
            print("previous player pos = ("+ str(
                                        round(previous_player_pos[0], 4)
                                        )+", "+str(
                                                round(previous_player_pos[1], 4)
                                                ) +")")
            print("number of bullets: "+ str(len(all_of_the_bullets)))

    pygame.time.delay(1000//FPS)
    total_num_of_ticks  += 1
    previous_player_pos  = [player_pos[0],  player_pos[1] ]
    previous_bubbles_pos = [bubbles_pos[0], bubbles_pos[1]]
#
print("")
print("")
print("- - - done - - -")
print("")

print("times bubbles killed: "+ str(times_bubbles_killed))