'''Day1 - Activity 5 _ LED Sparkles'''
# (c) HSLU 2021 Martin Vogel - martin.vogel@hslu.ch

from sense_hat import SenseHat
import time
import random

sense = SenseHat()


def get_random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


sense.clear()
i = 0
j = 0
pixel_liste = []

while True:
    # generate a random color and fill the matrix
    while i < 64:
        pixel_liste.append(get_random_color())
        i += 1
    sense.set_pixels(pixel_liste)
    time.sleep(0.5)
    sense.clear()
    i = 0
    pixel_liste = []
