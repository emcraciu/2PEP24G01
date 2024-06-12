import timeit


def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial2(n):
    if n <= 1:
        return 1
    else:
        return n * factorial2(n - 1)


x = list(range(1, 255))
factorial1_values = []
factorial2_values = []


def compare_factorials():
    for i in range(1, 255):
        rez = timeit.timeit(f'factorial1({i})', setup=f"from {__name__} import factorial1", number=100)
        factorial1_values.append(rez)

    print(factorial1_values)
