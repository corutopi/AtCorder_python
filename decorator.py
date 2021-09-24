import functools


def stop_watch(func):
    @functools.wraps(func)
    def wrapper(*arg, **kargs):
        from time import time
        start = time()
        result = func(*arg, **kargs)
        print('processing speed is :', time() - start, '(s)')
        return result

    return wrapper


if __name__ == '__main__':
    pass
