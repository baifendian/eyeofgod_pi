class Event(object):
    def __init__(self, sensor_type,sensor_id, pi_mark, timestamp,state) :
        self.sensor_type  = sensor_type
        self.sensor_id    = sensor_id
        self.pi_mark      = pi_mark
        self.timestamp    = timestamp
        self.state        = state
        self.mark         = pi_mark + '_' + sensor_id

    def buildMessage(self):
        message = {}
        message['sensor_type'] = self.sensor_type
        message['sensor_id'] = self.sensor_id
        message['pi_mark'] = self.pi_mark
        message['timestamp'] = self.timestamp
        message['state'] = self.state
        message['mark'] = self.mark
        return message
