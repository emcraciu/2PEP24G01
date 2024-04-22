"""Decorator to execute function only during working hours"""

from functools import wraps
import time


# decorator
def working_hours(start: int, stop: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            local_time = time.localtime().tm_hour
            if start < local_time < stop:
                func(*args, **kwargs)

        return wrapper

    return decorator


@working_hours(9, 20)
def alarm():
    print("Wake up!")


alarm()
