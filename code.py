"""
Created by: Sophie N
on: Apr 16

servo turns depending on distance from sonar
"""

import time
import board
import adafruit_hcsr04
import digitalio
import pwmio
import servo


# variables
distance = 0
servo_delay = 2
TOO_CLOSE = 20

# setup
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP15, echo_pin = board.GP14)

# create a PWMOut object on Pin GP12.
pwm = pwmio.PWMOut(board.GP12 , duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

# loop
while True:
    # Sonar gets the distance form object
    distance = sonar.distance

    # Turns on LED if an object’s distance is equal to or closer then 20 cm from the sonar
    if distance < TOO_CLOSE:
            my_servo.angle = 180
    else:
            my_servo.angle = 0

    time.sleep(servo_delay)