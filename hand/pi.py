
#coding:utf-8


import schedule
import sensor

import config




def main() :

    # schedule
    scheduler = schedule.Schedule()

    # config
    for (k,v) in config.SENSOR_MAP.items() :

        # new a sensor
        #sensor = sensor()

        # register a sensor
        #scheduler.register(sensor)
        scheduler.register(k,v)

    # list
    scheduler.list()

    # start scheduler
    print "[Schedule] start ..."

    scheduler.start()

    print "[Schedule] stop ..."





if __name__ == "__main__" : 
    main()



