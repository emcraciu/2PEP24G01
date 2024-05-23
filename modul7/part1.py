from threading import Thread

PRIME_RANGES = [[1000, 2000], [3000, 4000]]


def is_prime(number: int):
    for i in range(2, number // 2 + 1):
        if (number % i) == 0:
            return False
    return True


def primes(start_number: int, stop_number):
    result = []
    if not stop_number or not stop_number:
        start_number, stop_number = PRIME_RANGES.pop(0)
    for i in range(start_number, stop_number + 1):
        if is_prime(i):
            result.append(i)
    return result


class Client(Thread):

    def run(self):
        try:
            if self._target is not None:
                self.output = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

    def process_results(self):
        print(self.output)


class Server(Thread):

    def run(self):
        try:
            if self._target is not None:
                self.output = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

    def process_results(self):
        print(self.output)


prime1 = Client(target=primes, args=(None, None))
prime2 = Server(target=primes, args=(None, None))

for proc in [prime1, prime2]:
    proc.start()

for proc in [prime1, prime2]:
    proc.join()

for proc in [prime1, prime2]:
    proc.process_results()
