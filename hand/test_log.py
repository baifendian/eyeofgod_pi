import logging
from logging import config
import LOGGING
config.dictConfig(LOGGING.LOGGING)
mydict={'af':'asdf'}
distance=5
def test():
    logging.info('Out Of Range, %s' % (distance))
    print(mydict)
    logging.error("test")
test()
