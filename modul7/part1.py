from threading import Thread


def is_prime(number: int):
    for i in range(2, number // 2 + 1):
        if (number % i) == 0:
            return False
    return True


def primes(limit: int):
    result = []
    for i in range(1, limit + 1):
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


prime1 = Client(target=primes, args=(10000,))
prime2 = Server(target=primes, args=(10000,))

for proc in [prime1, prime2]:
    proc.start()

for proc in [prime1, prime2]:
    proc.join()

for proc in [prime1, prime2]:
    proc.process_results()
