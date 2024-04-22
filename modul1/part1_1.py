"""Need to change from cm units to inch"""
scale_factor = float(input("Give scale factor (2.54 for inch): "))
from functools import wraps


def decorator_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result / (scale_factor ** 2)

    return wrapper


@decorator_1
def area_1(length: int, width: int):
    return length * width

print(f"Area calculated with decorated function: {area_1(10, 10)}")
print(f'Function name: {area_1.__name__}')