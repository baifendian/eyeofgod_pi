import urllib
import urllib2
import time
from notice import *
message={ 'mark':'S-PI-2','state':0,'timestamp':int(time.time()) }
print message
Notice.notify(message)
