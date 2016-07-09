
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
        evt = None
        if GPIO.input(self.PINN) :
            now = time.time()
            if now - self.last > 5 :
                evt = event.Event(self.type, self.id, 1)
            self.last = now
        return evt


if __name__ == "__main__" :
    args = {"PINN" : 17}
    sensor = SensorMotion(1, 2, args)
    while True :
        time.sleep(1)
        print sensor.detect()


