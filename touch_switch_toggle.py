#!/usr/bin/env python
#this script uses the Touch Switch to toggle on/off sensors

import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Touch Switch; pin 31 = GPIO 6
touch_pin = 31

#set Touch Switch pin's mode as input
GPIO.setup(touch_pin,GPIO.IN)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

#set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)

#create Buzz function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,1000)

#create infinite loop that reads Touch Switch input
While True:
    if GPIO.input(touch_pin) == 0:
    Buzz.ChangeFrequency(440)
    Buzz.start(50)
    if GPIO.input(touch_pin) == 1:
    time.sleep(1)
    Buzz.stop()

    #reset GPIO resources used by script
    GPIO.cleanup()

