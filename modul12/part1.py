import timeit

from random import randint
import matplotlib.pyplot as plt
import math


def random_gen(num_iter):
    result = []
    for _ in range(num_iter):
        result.append(randint(10000, 20000))
        result.sort()
    return result


x = []
y = []

for i in range(1000, 3000, 100):
    result_time = timeit.timeit(f"random_gen({i})", setup="from __main__ import random_gen", number=100)
    print(result_time)
    x.append(i)
    y.append(result_time)

fig, (area1, area2) = plt.subplots(nrows=2, ncols=1, sharex="all")
fig.dpi = 200
area1.plot(x, y, label="Time take to generate numbers")
area2.plot(x, list(map(lambda y1: math.log(y1), y)), label="Time take to generate numbers")
area1.legend()
plt.xlabel("number of iterations ")
plt.ylabel("execution time")
plt.title("My Graph")
plt.show()
