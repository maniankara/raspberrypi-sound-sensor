#!/usr/bin/env python

import RPi.GPIO as GPIO
import spidev
import time, sys

sound = 0
led = 17

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1
spi.mode = 1

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)
#GPIO.setup(led,GPIO.OUT)

def readadc(adcnum):
    r = spi.xfer2([1, 8+adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8 ) + r[2]
    return adcout

a = []
try:
    while True:
        x = readadc(sound)
        a.append(x)
        if len(a) == 1000:
            print("max is: ", max(a))
            a = []
        # if (x > 250):
        #     GPIO.output(led,False)
        #     time.sleep(1)
        # else:
        #     GPIO.output(led, True)
except KeyboardInterrupt:
    spi.close()
    GPIO.cleanup()
    sys.exit(1)