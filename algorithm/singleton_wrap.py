from functools import wraps
from threading import Lock

def singleton(cls):
    """装饰类的装饰器"""
    instances={}

    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
            print(instances)
        return instances[cls]

    return wrapper


def singleton2(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class President():
    pass

if __name__ == '__main__':
    p1 = President()
    print(p1)
    p2 = President()
    print(p2)