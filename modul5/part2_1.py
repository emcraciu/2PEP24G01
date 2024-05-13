import asyncio
import time
from random import randint
var = []


async def function1(a, b):
    if a:
        number = randint(1, 5)
        await asyncio.sleep(number)
        var.append(1)
    if b:
        number = 2
        await asyncio.sleep(number)
        var.append(2)


async def function2():
    while len(var) < 4:
        print(var)
        await asyncio.sleep(0.5)


async def main():
    start = time.time()
    tasks = await asyncio.gather(function1(1, 0), function1(0, 1), function1(1,1), function2())

    print(tasks)
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    asyncio.run(main())
