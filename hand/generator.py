import urllib
import urllib2
import time
from notice import *
mydict={}
for i in range(1,47):
    mydict[i]=0
while True:
    for i in range(1,47):
        message={}
        message['mark']='b8:27:eb:e0:e1:cf'+str(i)
        message['state']=mydict[i]
        mydict[i] = (mydict[i] +1)%2
        message['timestamp']=int(time.time())
        Notice.notify(message)
        time.sleep(1)
