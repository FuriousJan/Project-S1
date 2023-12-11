from sense_hat import Sensehat
import random
import sys
import pygame
from pygame.locals import *

sense = Sensehat()

r = (255, 0, 0)
sense,set_pixel(0,0, r)
pixel_list = sense.get_pixels()
if __name__ == "__main__":


