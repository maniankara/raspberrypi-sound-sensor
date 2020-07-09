#!/usr/bin/env python

import RPi.GPIO as GPIO
import spidev
import time, sys

sound = 0
led = 7

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000
spi.mode = 1

#GPIO.setwarnings(True)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(sound, GPIO.IN)
#GPIO.setup(led,GPIO.OUT)

def readadc(adcnum):
    #r = spi.xfer2([1, 8+adcnum << 4, 0])
    r = spi.xfer2([0xc4,0x00,0x00,0x00])
    print "r is: ", r, " channel: ", adcnum
    adcout = ((r[1] & 3) << 8 ) + r[2]
    return adcout

try:
    while True:
        for i in range(8):
            readadc(i)
            time.sleep(0.2)
        # x = readadc(sound)
        # print "x is: ", x
        # time.sleep(0.1)
        # if (x > 250):
        #     GPIO.output(led,False)
        #     time.sleep(1)
        # else:
        #     GPIO.output(led, True)
except KeyBoardInterrupt:
    spi.close()
    sys.exit(1)