# moves one pixel with a red color around the led field
# with the input of the keyboards arrows up, down, left, right
# Martin Vogel - martin.vogel@hslu.ch

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

red = (255, 0, 0)
wht = (255, 255, 255)
led_matrix = []


def set_matrix(x_pos, y_pos, p_color, bk_ground):
    matrix = []
    i = 0
    j = 0
    while i < 8:
        while j < 8:
            if i == x_pos and j == y_pos:
                matrix.append(p_color)
            else:
                matrix.append(bk_ground)
            j += 1
        j = 0
        i += 1
    return matrix


sense.clear()
sleep(1)
x = 4
y = 4
sense.set_pixels(set_matrix(x, y, red, wht))

while True:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            # Check which direction
            if event.direction == "up":
                if x == 0:
                    x = 7
                else:
                    x -= 1
                print("up", x)
            elif event.direction == "down":
                if x == 7:
                    x = 0
                else:
                    x += 1
                print("down", x)
            elif event.direction == "left":
                if y == 0:
                    y = 7
                else:
                    y -= 1
                print("left", y)
            elif event.direction == "right":
                if y == 7:
                    y = 0
                else:
                    y += 1
                print("right", y)
            elif event.direction == "middle":
                print("middle")

            # Wait a while and then clear the screen
            sense.set_pixels(set_matrix(x, y, red, wht))
            sleep(0.1)



