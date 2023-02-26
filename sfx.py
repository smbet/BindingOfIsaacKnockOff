import pygame
import os

def get_shooty(samplename='laser_short_dry.wav'):
	laser_short_dry = pygame.mixer.Sound('./../audio/'+samplename) # this will need to be fixed with os to work on everyones shit
	return(laser_short_dry)

def shooty(sample):
	sample.play()
	sample.set_volume(0.8)
	return

	