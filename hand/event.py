import uuid
import time
class Event :

    def __init__(self, sensor_type,sensor_id, state,timestamp=int(time.time())) :
        self.sensor_type  = sensor_type
        self.sensor_id    = sensor_id
        self.pi_mark      = self.getMac()
        self.timestamp    = timestamp
        self.state        = state
        self.mark         = self.pi_mark + '_' + str(self.sensor_id)

    #get mac address
    def getMac(self):
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e+2] for e in range(0,11,2)])

    def buildMessage(self):
        message = {}
        message['sensor_type'] = self.sensor_type
        message['sensor_id'] = self.sensor_id
        message['pi_mark'] = self.pi_mark
        message['timestamp'] = self.timestamp
        message['state'] = self.state
        message['mark'] = self.mark
        return message
