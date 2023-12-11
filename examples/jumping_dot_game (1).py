# tiny game to use the joystick of the sensehat
# mouse focus needs to be in the emulator to use the keyboard
# Michael Handschuh original source

import sense_hat
import time
from random import randint

sense = sense_hat.SenseHat()
sense.set_rotation(270)
sense.clear()

blue = (0, 0, 255)
yellow = (255, 255, 0)
clear = (0, 0, 0)

up_key = sense_hat.DIRECTION_UP
pressed = sense_hat.ACTION_PRESSED

bottom_y = 7

pos_x = 3
pos_y = bottom_y

ball_x = 7
ball_y = bottom_y

debug_mode = True
game_over = False
setup = True
jumping = False


def debug_message(message):
    if debug_mode:
        print(message)


def draw_player():
    debug_message("drawing player")
    sense.set_pixel(pos_x, pos_y, blue)


def draw_ball():
    debug_message("drawing ball")
    sense.set_pixel(ball_x, ball_y, yellow)


def clear_background(color=clear):
    debug_message("clearing background")
    sense.clear(clear)


def draw_scene():
    clear_background()
    draw_player()
    draw_ball()


def move_ball():
    global ball_x, game_over, pos_x, pos_y
    debug_message("moving ball")
    ball_x -= 1  # Move ball left
    if ball_x < 0:  # Check if ball is at left border move it to the right side
        ball_x = 7
    if ball_x == pos_x and pos_y == bottom_y:  # Check if ball hits player
        game_over = True


last_tick = round(time.time(), 1) * 10
# Main game loop
while True:
    if game_over:
        sense.show_message("GAME OVER")
        game_over = False
        setup = True

    if setup:
        pos_x = 3
        ball_x = 7
        ball_y = 7
        draw_scene()

        setup = False

    timer = 10
    tick = round(time.time(), 1) * 10
    if(tick % 30 == 0) and (tick > last_tick):  # approx. after 3 seconds reset jump (gravity)
        if jumping:
            pos_y += 1
            jumping = False
    if(tick % timer == 0) and (tick > last_tick):  # approx. every second move the ball
        move_ball()
        draw_scene()
        last_tick = tick

    events = sense.stick.get_events()
    if events:
        for e in events:
            debug_message("Processing joystick events")
            if e.direction == up_key and e.action == pressed:  # check if jumping
                debug_message("Joystick up press detected")
                # only jump if not already jumping (otherwise you would fly!)
                if not jumping:
                    pos_y -= 1
                    jumping = True
                draw_scene()
