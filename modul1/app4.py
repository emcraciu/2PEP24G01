""" Keep track of how many times a function is called """

from functools import wraps


def count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'Function {func.__name__} was called: {wrapper.calls} times')
        return func(*args, **kwargs)

    wrapper.calls = 0
    wrapper.calls_1 = []
    return wrapper


@count
def area(length: int, width: int):
    return length * width


# area = count(area)
area(1, 1)
area(2, 2)
area(3, 3)
area(4, 4)
print(area.calls)
area.calls_1.append(10)
print(area.calls_1)
