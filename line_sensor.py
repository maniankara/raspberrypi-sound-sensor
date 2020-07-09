#!/usr/bin/env python3

from gpiozero import LineSensor
from signal import pause

sensor = LineSensor(22)
sensor.when_line = lambda: print("Line detected", sensor.value)
sensor.when_no_line = lambda: print('No line detected', sensor.value)
pause()
