'''Day1 - Activity 1 u.a'''
# alarm according the temperature indicated on the display
# (c) HSLU 2021 Martin Vogel - martin.vogel@hslu.ch

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(270)

# definition of LED color codes
X = (255, 0, 0)  # Red
O = [255, 255, 255]  # White

red = (255, 0, 0)
wht = (255, 255, 255)
blk = (0, 0, 0)
ylw = (255, 255, 0)
blu = (0, 0, 255)
grn = (0, 255, 0)

while True:
    temp = sense.get_temperature()

    temp = round(temp, 2)

    if temp > 26:
        color = red
    elif temp > 20:
        color = ylw
    elif temp < 0:
        color = blu
    else:
        color = grn

    temp = str(temp)

    sense.show_message(temp, text_colour=color)




