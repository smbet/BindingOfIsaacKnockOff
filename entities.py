import pygame
import random

import essential_global_variables
# from definately_not_a_knockoff_main import player
# from pygame_initialization import the_pygame_init



player_pos         = [essential_global_variables.WIDTH / 2, essential_global_variables.HEIGHT / 2]
player = pygame.image.load("resources/moon_50x50.png").convert()
PLAYER_WIDTH       = pygame.Surface.get_width(player)
PLAYER_HEIGHT      = pygame.Surface.get_height(player)
PLAYER_SPEED          = 300
player_speed_variable = 0
player_rectangle   = pygame.Rect(
                                 player_pos[0],
                                 player_pos[1],
                                 PLAYER_WIDTH,
                                 PLAYER_HEIGHT
                                 )


bubbles            = pygame.image.load("resources/Bubbles_50x50.png").convert()
bubbles_pos        = [essential_global_variables.WIDTH * random.random(), essential_global_variables.HEIGHT * random.random()]
BUBBLES_WIDTH      = pygame.Surface.get_width(bubbles)
BUBBLES_HEIGHT     = pygame.Surface.get_height(bubbles)
BUBBLES_SPEED         = PLAYER_SPEED / 2
BUBBLES_COOLDOWN      = 0 # number of ticks that bubbles is immune after respawning
bubbles_rectangle  = pygame.Rect(
                                 bubbles_pos[0],
                                 bubbles_pos[1],
                                 BUBBLES_WIDTH,
                                 BUBBLES_HEIGHT
                                 )