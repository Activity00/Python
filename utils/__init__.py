import time


def time_this(t_type='s'):
    def wrapper_out(func):
        def wrapper(*args, **kwargs):
            t = time.clock()
            ret = func(*args, **kwargs)
            if t_type == 'ms':
                print('总用时: %f ms' % ((time.clock() - t)*1000))
            else:
                print('总用时: %f s' % (time.clock() - t))
            return ret
        return wrapper
    return wrapper_out
