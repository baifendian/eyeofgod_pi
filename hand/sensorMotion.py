

import sensor
import RPi.GPIO as GPIO


class SensorMotion(sensor.Sensor) :

    def __init__(self, args) :
        self.PINN = args["PINN"]
        GPIO.setmode(GPIO.BCD)
        GPIO.setup(PINN, GPIO.IN)

    def detect(self) :
        if GPIO.input(self.PINN) :
            print "True"
            return True
        else :
            return Flase


if __name__ == "__main__" :
    args = {"PINN" : 18}
    sensor = SensorMotion(args)
    sensor.detect()


