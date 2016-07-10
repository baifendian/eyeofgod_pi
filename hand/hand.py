
#coding:utf-8


import piconfig
import schedule
import sensorDistance
import sensorMotion
import logging
from logging import config
import LOGGING
config.dictConfig(LOGGING.LOGGING)



def main() :

    # schedule
    scheduler = schedule.Schedule()

    # load sensor
    for (id,info) in piconfig.SENSOR_MAP.items() :

        mname   = info["module"]
        cname   = info["clazz"]

        module  = __import__(mname)
        clazz   = getattr(module, cname)

        # new a sensor
        sensor  = clazz(id, info["type"], info["args"])

        # register a sensor
        scheduler.register(id, sensor)

    # list
    scheduler.list()

    # start scheduler
    logging.info( "[Schedule] start ...")

    scheduler.start()

    logging.info("[Schedule] stop ...")




if __name__ == "__main__" : 
    main()



