

import config
import urllib
import urllib2


#message: { 'id':$id , 'distance':$distance }


#the tool class to dispatch message to  server
class Notice :

    #def __init__(self) :
    #    self.url = config.SERVER_URL


    @staticmethod
    def notify(message):
        ms_encode = urllib.urlencode(message)
        req = urllib2.Request(config.SERVER_URL, ms_encode)
        sock = urllib2.urlopen(req)
        html = sock.read()
        code = sock.getcode()
        sock.close()
        print html
        print code
        return code
