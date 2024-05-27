"calculate factorial with recursive function and create 10 threads with this function"
numbers = [num for num in range(10, 20)]
# Calculate factorial with recursive function and create 10 threads with this function
from threading import RLock, Thread


class Factorial(Thread):

    def run(self):
        try:
            self.output = self.calculate_factorial(*self._args)
        finally:
            del self._target, self._args, self._kwargs

    def calculate_factorial(self, n, lock: RLock):
        if n <= 1:
            return 1
        else:
            lock.acquire()
            try:
                result = n * self.calculate_factorial(n - 1, lock)
                with open("text.log", "a") as file:
                    file.write("called function recursively" + "\n")
            finally:
                lock.release()
            return result


f = Factorial()
rlock = RLock()

threads = []

for num in numbers:
    thd = Factorial(target=lambda: True, args=(num, rlock))
    thd.start()
    threads.append(thd)

for thd in threads:
    thd.join()

for thd in threads:
    print(thd.output)
