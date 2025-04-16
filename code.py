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
servo_delay = 0.5
TOO_CLOSE = 50

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
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(servo_delay)
    else:
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(servo_delay)