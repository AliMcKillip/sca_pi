#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for AUto FLash LEd pin 11 = GPIO 17
led_pin = 11

#set Auto Flash Led pin's mode as output
GPIO.setup(led_pin,GPIO.OUT)

#turn on AUto FLash LEd
GPIO.output(led_pin,True)
time.sleep(2)

#turn off AUto Flash LED
GPIO.output(led_pin,True)
time.sleep(2)

#turn off Auto FLash LED
GPIO.output(led_pin,False)

#reset GPIO resources used by script
GPIO.cleanup()
