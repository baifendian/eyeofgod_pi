
# coding:utf-8


import time
import sensor
import notice


class Schedule :

    def __init__(self) :
        self.sensors = {}
        self.notifier = notice.Notice()


    def register(self, id, sensor) :
        self.sensors[id] = sensor


    def unregister(self, id) :
        return self.sensors.pop(id)


    def list(self) :
        for (k,v) in self.sensors.items() :
            print k,v


    def start(self) :
        while True :
            time.sleep(1)
            for (id,sensor) in self.sensors.items() :
                try :
                    event = sensor.detect()
                    if event :
                        print id, sensor
                        self.notifier.notify(message)
                except Exception,ex :
                    pass


    def stop(self) :
        pass



if __name__ == "__main__" :

    print "===================="
    scheduler = Schedule()

    scheduler.register(1, "sensor1")
    scheduler.register(2, "sensor2")
    scheduler.register(3, "sensor3")
    scheduler.register(4, "sensor4")
    scheduler.register(5, "sensor5")

    print "===================="
    scheduler.list()

    scheduler.unregister(2)
    scheduler.unregister(3)

    print "===================="
    scheduler.list()

    print "===================="
    scheduler.start()





