#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

s = "Hello World!"
speed = 0.01

while True:
    sense.show_message(s, speed)
    guess = raw_input("What is your guess?")
    if s == guess:
        print "Win! Scroll Speed:", speed
        break
    else: 
        speed = speed + 0.01
        print 'Incorrect'
