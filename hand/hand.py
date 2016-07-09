
#coding:utf-8


import config
import schedule
import sensorDistance
import sensorMotion




def main() :

    # schedule
    scheduler = schedule.Schedule()

    # load sensor
    for (id,info) in config.SENSOR_MAP.items() :

        mname   = info["module"]
        cname   = info["clazz"]

        module  = __import__(mname)
        clazz   = getattr(module, cname)

        # new a sensor
        sensor  = clazz()

        # register a sensor
        scheduler.register(id, sensor)

    # list
    scheduler.list()

    # start scheduler
    print "[Schedule] start ..."

    scheduler.start()

    print "[Schedule] stop ..."




if __name__ == "__main__" : 
    main()



