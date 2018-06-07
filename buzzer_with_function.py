#!/usr/bin/env python
#this script turns the Passive Buzzer on and then off using two sound frequencies 

import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

#set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)

#create Buzz function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,1000)

#define buzz() subroutine
def buzz(freq):
    Buzz.ChangeFrequency(freq)
    Buzz.start(50)
    time.sleep(1)
    Buzz.stop()

#run buzz() and send it a frequency to use
buzz(440)
buzz(880)

#reset GPIO resources used by script
GPIO.cleanup()
