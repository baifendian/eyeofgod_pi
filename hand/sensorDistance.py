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
import traceback
import RPi.GPIO as GPIO

from event import Event
from sensor import Sensor

#TODO: REMOVE TO CONFIGURE
# Speed
SPEED = 17150

class SensorDistance(Sensor):
    def __init__(self, _id='none', _type='none', _args={}):
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

        self.id = _id
        self.type = _type
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
            print traceback.print_exc
            GPIO.cleanup()
            return None
        
        start_time = 0;
        end_time = 0;
        while 0 == self.GPIO.input(self.echo):
            start_time = time.time()

        while 1 == self.GPIO.input(self.echo):
            end_time = time.time()
        if start_time == 0 or end_time == 0:
            print 'missassignment'
            GPIO.cleanup()
            return None

        distance = round((end_time - start_time) * SPEED, 2)
        if distance < 1 or distance > 4000:
            print 'Out Of Range, %s' % (distance)
            GPIO.cleanup()
            return None

        print 'Distance: %s cm.' % (distance - 0.5)
        flag = True
        if distance > self.args['LIMIT']:
            flag = False

        event = Event(self.id, self.type, flag, int(time.time()))

        GPIO.cleanup()
        return event.buildMessage()

if __name__ == '__main__':
    dict_example = {"ECHO": 24, "TRIG": 23, "LIMIT": 20}
    sensor = SensorDistance('dist', '001', dict_example)
    print sensor.detect()

