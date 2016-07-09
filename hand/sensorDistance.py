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

import event
from sensor import Sensor

#TODO: REMOVE TO CONFIGURE
# Speed
SPEED = 17150

class Sensor(Sensor):
    def __init__(self, _args):
        '''
        Dict example
        "args": { 
            "ECHO" : 11, 
            "TRIG" : 12, 
            "LIMIT" : 20
         }
        '''
        # Set board to BCM mode
        GPIO.setmode(GPIO.BCM)

        self.trig = int(_args['TRIG'])
        self.echo = int(_args['ECHO'])

        # Set pin as GPIO out
        GPIO.setup(self.trig, GPIO.OUT)
        # Set pin as GPIO in
        GPIO.setup(self.echo, GPIO.IN)

        self.GPIO = GPIO
        self.args = _args

    def detect(self):
        try:
            self.GPIO.output(self.trig, False)
            print 'Sensor will be starting...'
            time.sleep(1)

            # Testing for sensor
            self.GPIO.output(self.trig, True)
            time.sleep(0.00001)
            self.GPIO.output(self.trig, False)
            print 'Sensor is ready'
        except Exception:
            self.GPIO.cleanup()
            print 'GPIO Exception'
            return None

        while 0 == self.GPIO.input(self.echo):
            #print 'first input'
            start_time = time.time()

        while 1 == self.GPIO.input(self.echo):
            #print 'second input'
            end_time = time.time()

        distance = round((end_time - start_time) * SPEED, 2)

        if distance < 1 or distance > 4000:
            print 'Out Of Range'
            return None

        print 'Distance: %s cm.' % (distance - 0.5)

if __name__ == '__main__':
    dict_example = {"ECHO": 23, "TRIG": 24, "LIMIT": 20}
    sensor = Sensor(dict_example)
    sensor.detect()

