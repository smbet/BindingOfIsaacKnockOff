import pygame
import math

the_pygame_init = pygame.init()

SIZE = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(SIZE)

FPS = 30

SPEED_CORRECTION      = 1 / math.sqrt(2)