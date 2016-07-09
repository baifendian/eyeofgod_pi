
# coding:utf-8


import time
import event
import sensor
import notice


class Schedule :

    def __init__(self) :
        self.sensors = {}
        #self.notifier = notice.Notice()


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
            print "----------------------"
            for (id,sensor) in self.sensors.items() :
                try :
                    evt = sensor.detect()
                    if evt is not None :
                        print id, sensor
                        message = evt.buildMessage()
                        notice.Notice.notify(message)
                except Exception,ex :
                    print ex
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





