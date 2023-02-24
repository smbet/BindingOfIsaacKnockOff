import pygame
import random

import essential_global_variables



# player_pos         = [essential_global_variables.WIDTH / 2, essential_global_variables.HEIGHT / 2]
player = pygame.image.load("resources/moon_50x50.png").convert()
PLAYER_WIDTH          = pygame.Surface.get_width(player)
PLAYER_HEIGHT         = pygame.Surface.get_height(player)
PLAYER_SPEED          = 300
player_speed_variable = 0
player_rectangle      = pygame.Rect(
                                    essential_global_variables.player_pos[0],
                                    essential_global_variables.player_pos[1],
                                    PLAYER_WIDTH,
                                    PLAYER_HEIGHT
                                    )


bubbles           = pygame.image.load("resources/Bubbles_50x50.png").convert()
# bubbles_pos       = [essential_global_variables.WIDTH * random.random(), essential_global_variables.HEIGHT * random.random()]
BUBBLES_WIDTH     = pygame.Surface.get_width(bubbles)
BUBBLES_HEIGHT    = pygame.Surface.get_height(bubbles)
BUBBLES_SPEED     = PLAYER_SPEED / 2
BUBBLES_COOLDOWN  = 0 # number of ticks that bubbles is immune after respawning
bubbles_rectangle = pygame.Rect(
                                essential_global_variables.bubbles_pos[0],
                                essential_global_variables.bubbles_pos[1],
                                BUBBLES_WIDTH,
                                BUBBLES_HEIGHT
                                )