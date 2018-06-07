#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.show_letter("H", (255, 0, 0))
time.sleep(1)
sense.show_letter("i", (255, 255, 255))
time.sleep(1)
sense.show_letter("!", (0, 0, 255))
time.sleep(1)
sense.clear()
