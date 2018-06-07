#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.randint(0,255)
s = random.randint(0,255)
g = random.randint(0,255)

sense.show_letter("H", (r, s, g))
time.sleep(1)
sense.show_letter("i", (g, r, s))
time.sleep(1)
sense.show_letter("!", (s, g, r))
time.sleep(1)

sense.clear()
