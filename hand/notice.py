import urllib
import urllib2

#message: { 'id':$id , 'distance':$distance }

#the tool class to dispatch message to  server
class Notice :

    #def __init__(self) :
        # need do nothine
    #    pass


    @staticmethod
    def notify(message):
        url = "http://192.168.1.140:9000/sensor/postdata"
        ms_encode = urllib.urlencode(message)
        req = urllib2.Request(url,ms_encode)
        sock = urllib2.urlopen(req)
        html = sock.read()
        code = sock.getcode()
        sock.close()
        print html
        print code
        return code
