"""Need to change from cm units to inch"""
scale_factor = 2.54
def area(length: int, width: int):
    return length * width

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result / (2.54**2)

    return wrapper

if __name__ == '__main__':
    # in cm
    result_in_cm = area(10, 10)
    print(f'Result in CM: {result_in_cm}')

    result_in_in = result_in_cm/(2.54**2)
    print(f'Result in inch: {result_in_in}')

    if scale_factor != 1:
        area = decorator(area)
    print(type(area))

    new_result = area(10, 10)
    print(f'Result in inch from wrapped function: {new_result}')

    # area(10, 10)


