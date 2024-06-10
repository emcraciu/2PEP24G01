"""Createdecorator for adding customisable delay in function resonse """

from time import sleep
from functools import wraps

test_cond = True

def delay(seconds=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@delay(seconds=5)
def area(length: int, width: int):
    return length * width


if __name__ == "__main__":
    print(area(10, 10))
