import asyncio
import time
from random import randint


async def function1():
    number = randint(1, 5)
    await asyncio.sleep(number)
    print(number, function1.__name__)
    await asyncio.sleep(number)
    print(number, function1.__name__ + " step2")
    return 1


async def function2():
    await asyncio.sleep(2)
    print(function2.__name__)
    await asyncio.sleep(2)
    print(function2.__name__ + " step2")
    return 2


async def function3():
    await asyncio.sleep(3)
    print(function3.__name__)
    await asyncio.sleep(4)
    print(function3.__name__ + " step2")
    return 3


async def main():
    start = time.time()
    # tasks = await asyncio.gather(function1(), function2(), function3())
    tasks = await asyncio.gather(function1(), function1(), function1(), function1())

    print(tasks)
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    asyncio.run(main())
