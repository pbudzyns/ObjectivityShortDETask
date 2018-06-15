from time import time


def timing(f):
    def wrap(*args):
        time1 = time()
        ret = f(*args)
        time2 = time()
        print('%s function took %f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap
