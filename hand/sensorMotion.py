
import time
import event
import sensor
import RPi.GPIO as GPIO


class SensorMotion(sensor.Sensor) :

    def __init__(self, id, type, args) :
        self.id   = id
        self.type = type
        self.PINN = args["PINN"]
        self.last = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PINN, GPIO.IN)

    def detect(self) :
        if GPIO.input(self.PINN) :
            now = time.time()
            if now - self.last > 5 :
                print "True"
                self.last = now
                return True
            else :
                print "Wait"
                self.last = new
        else :
            print "False"
            return False


if __name__ == "__main__" :
    args = {"PINN" : 18}
    sensor = SensorMotion(args)
    sensor.detect()


