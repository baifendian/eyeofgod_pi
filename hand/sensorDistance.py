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
    def __init__(self, judge):
        # Set board to BCM mode
        GPIO.setmode(GPIO.BCM)
        # Set pin as GPIO out
        GPIO.setup(TRIG, GPIO.OUT)
        # Set pin as GPIO in
        GPIO.setup(ECHO, GPIO.IN)

        self.GPIO = GPIO
        self.judge = judge

    def detect(self):
        try:
            self.GPIO.output(TRIG, False)
            print 'Sensor will be starting...'
            time.sleep(1)

            # Testing for sensor
            self.GPIO.output(TRIG, True)
            time.sleep(0.00001)
            self.GPIO.output(TRIG, False)
            print 'Sensor is ready'
        except Exception:
            self.GPIO.cleanup()
            return None

        while 0 == self.GPIO.input(ECHO):
            start_time = time.time()

        while 1 == self.GPIO.input(ECHO):
            end_time = time.time()

        distance = round((end_time - start_time) * SPEED, 2)

        if distance < 1 or distance > 4000:
            print 'Out Of Range'
            return None

        print 'Distance: %s cm.' % (distance - 0.5)


if __name__ == '__main__':
    sensor = Sensor()
    sensor.detect()

