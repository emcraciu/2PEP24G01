from functools import wraps


def unit_decorator(unit: str):
    if unit == 'cm':
        scale_factor = 1
    elif unit == 'inch':
        scale_factor = 2.54
    elif unit == 'mm':
        scale_factor = 0.1

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result / (scale_factor ** 2)

        return wrapper

    return decorator


@unit_decorator('inch')
def area(length: int, width: int):
    return length * width


@unit_decorator('mm')
def circle_area(radius):
    return 3.14 * (radius ** 2)


print(f"Area calculated with decorated function: {area(10, 10)}")
print(f'Function name: {area.__name__}')

print(f"Area or circle with decorated function: {circle_area(10)}")
print(f'Function name: {circle_area.__name__}')
