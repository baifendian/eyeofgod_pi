



SERVER_HOST = "192.168.1.140"
SERVER_PORT = "9000"
SERVER_PATH = "/sensor/postdata"
SERVER_URL  = "http://" + SERVER_HOST + ":" + SERVER_PORT + SERVER_PATH


SENSOR_MAP = {
    "3" : {
        "type"  : 1, 
        "module": "sensorDistance",
        "clazz" : "SensorDistance", 
        "args"  : {
            "ECHO" : 24, 
            "TRIG" : 23,
            "LIMIT" : 20
        }
    },
    "4" : {
        "type"  : 2,
        "module": "sensorMotion",
        "clazz" : "SensorMotion",
        "args"  : {
            "PINN" : 17
        }
    }
}



if __name__ == "__main__" :
    print SERVER_URL
