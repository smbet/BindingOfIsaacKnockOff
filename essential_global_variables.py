import pygame
import math


the_pygame_init = pygame.init()

SIZE = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(SIZE)

FPS = 30

clock = pygame.time.Clock()
dt    = clock.tick(FPS)



SPEED_CORRECTION      = 1 / math.sqrt(2)

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
bubbles_hit_tick     = 0
player_hit_tick      = 0
times_bubbles_killed = 0
total_num_of_ticks   = 0
the_game_is_running  = True