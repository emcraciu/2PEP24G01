import timeit
import matplotlib.pyplot as plt


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
        rez2 = timeit.timeit(f"factorial2({i})", setup=f"from {__name__} import factorial2", number=100)
        factorial2_values.append(rez2)

    print(factorial1_values)
    print(factorial2_values)
    fig, (area1, area2) = plt.subplots(nrows=2, ncols=1, sharex="all")
    fig.dpi = 200
    area1.plot(x, factorial1_values, label="Time taken to generate factorial1")
    area2.plot(x, factorial2_values, label="Time taken to generate factorial2")
    area1.legend()
    area2.legend()
    plt.xlabel("Input values")
    plt.ylabel("execution time")
    plt.title("My Graph")
    plt.show()
