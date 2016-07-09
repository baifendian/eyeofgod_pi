#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    <+ MODULE_NAME +>
    Distance Sensor

    <+ DESCRIPTION +>
    distance sensor

    Licensed under the <+ LICENSE +> license, see <+ X +> for more details etc.
    Copyright by EyeofGod
"""

import time
import RPi.GPIO as GPIO

from sensor import Sensor

#TODO: REMOVE TO CONFIGURE

#Associate pin 23 to TRIG
TRIG = 23
#Associate pin 24 to ECHO
ECHO = 24
# Speed
SPEED = 17150

class Sensor(Sensor):
    def __init__(self) :
        # Set board to BCM mode
        GPIO.setmode(GPIO.BCM)
        # Set pin as GPIO out
        GPIO.setup(TRIG,GPIO.OUT)
        # Set pin as GPIO in
        GPIO.setup(ECHO,GPIO.IN)

    def detect(self):
        GPIO.output(TRIG, False)
        print 'Sensor will be starting...'
        time.sleep(1)

        # Testing for sensor
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        print 'Sensor is ready'

        while 0 == GPIO.input(ECHO):
            start_time = time.time()

        while 1 == GPIO.input(ECHO):
            end_time = time.time()

        distance = round((end_time - start_time) * SPEED, 2)

        if distance < 2 or distance > 400:
            print 'Out Of Range'
            return NULL

        print 'Distance: %s cm.' % (distance-0.5)



if __name__ == '__main__':
    sensor = Sensor()

