# very first step of displaying a message on the led matrix
# Martin Vogel - martin.vogel@hslu.ch
# runs only on the trinket: https://trinket.io/sense-hat


from sense_hat import SenseHat
import time

s = SenseHat()
s.set_rotation(270)

s.show_message("This is going to be fun :-)")