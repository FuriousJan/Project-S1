from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Set up initial game state
bird_position = 4
bird_velocity = 0
gravity = 0.1
jump_strength = -2
obstacle_position = 7
obstacle_speed = 0.1
score = 0

def display_game_over_message():
    game_over_msg = "Game Over! Score: {}".format(score)
    sense.show_message(game_over_msg, text_colour=(255, 0, 0))

# Game loop
while True:
    # Read accelerometer data
    acceleration = sense.get_accelerometer_raw()
    y_acceleration = acceleration['y']

    # Update bird position based on accelerometer data
    bird_velocity += y_acceleration + gravity
    bird_position += int(bird_velocity)

    # Ensure bird stays within the screen boundaries
    bird_position = max(0, min(bird_position, 7))

    # Move obstacle to the left
    obstacle_position -= obstacle_speed

    # Check for collision with obstacle
    if obstacle_position <= 0:
        obstacle_position = 7
        obstacle_speed = 0.1 + randint(0, 5) / 10.0
        score += 1

    # Check for collision with bird
    if int(obstacle_position) == 4 and bird_position == 4:
        # Game over
        display_game_over_message()
        break

    # Create an empty pixel list
    pixels = [(0, 0, 0)] * 64

    # Set pixel for bird
    pixels[4 * 8 + bird_position] = (255, 0, 0)

    # Set pixel for obstacle
    pixels[int(obstacle_position) * 8 + 7] = (0, 255, 0)

    # Display the pixel list on the Sense HAT
    sense.set_pixels(pixels)

    # Pause for a short duration
    sleep(0.1)
