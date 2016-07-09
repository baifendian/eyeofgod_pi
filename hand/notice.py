

import piconfig
import urllib
import urllib2
import logging
from logging import config
import LOGGING
config.dictConfig(LOGGING.LOGGING)
#message: { 'id':$id , 'distance':$distance }


#the tool class to dispatch message to  server
class Notice :

    #def __init__(self) :
    #    self.url = config.SERVER_URL


    @staticmethod
    def notify(message):
        ms_encode = urllib.urlencode(message)
        req = urllib2.Request(piconfig.SERVER_URL, ms_encode)
        sock = urllib2.urlopen(req)
        html = sock.read()
        code = sock.getcode()
        sock.close()
        logging.debug(html)
        logging.debug(code)
        return code
