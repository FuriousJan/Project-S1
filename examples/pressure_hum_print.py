'''Day1 - Activity 1 u.a'''
# (c) HSLU 2021 Martin Vogel - martin.vogel@hslu.ch
# prints sensor values on the console

from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    pressure = sense.get_pressure()

    pressure = round(pressure, 1)

    humidity = sense.get_humidity()

    humidity = round(humidity, 2)

    print("Pressure: " + str(pressure) + " hPa --- Humidity: " + str(humidity) + " %")

    time.sleep(0.5)




