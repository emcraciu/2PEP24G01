import random
from threading import Thread
import socket


def is_prime(number: int):
    for i in range(2, number // 2 + 1):
        if (number % i) == 0:
            return False
    return True


def primes(start_number: int, stop_number):
    result = []
    for i in range(start_number, stop_number + 1):
        if is_prime(i):
            result.append(i)
    return result


class Connect:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket()
        self.host = host
        self.port = port

    def generate_prime(self):
        primes_list = primes(100000, 200000)
        self.prime = random.choice(primes_list)

    def get_prime(self, prime):
        if not getattr(self, "prime", False):
            self.prime = prime
            print(f'received prime: {self.prime}')
        else:
            raise AttributeError('Value for prime already set to:', self.prime)

    def generate_base(self):
        if getattr(self, "prime", False):
            self.base = random.randint(2, self.prime - 1)
        else:
            raise AttributeError('Value for prime needs to be set first')

    def get_base(self, base):
        if not getattr(self, "base", False):
            self.base = base
            print(f'received base: {self.base}')
        else:
            raise AttributeError('Value for base already set to:', self, base)

    def generate_local_secret(self):
        self.__local_secret = random.randint(2, self.prime)
        local_factor = pow(self.base, self.__local_secret) % self.prime
        print(self.__class__.__name__, local_factor)
        return local_factor

    def get_secret(self, secret):
        self.__shared_secret = pow(secret, self.__local_secret) % self.prime + 129
        print(self.__class__.__name__, "Shared secret: ", self.__shared_secret)

    def send_encrypted_message(self, message):
        # my code
        pass


class Client(Connect):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.sock.connect((self.host, self.port))
        self.generate_prime()
        self.generate_base()

    def start(self):
        self.thd = Thread(target=self.communicate)
        self.thd.start()

    def communicate(self):
        self.sock.send(bytes(f'{self.prime}', encoding="UTF-8"))
        self.sock.send(bytes(f'{self.base}', encoding="UTF-8"))
        local = self.generate_local_secret()
        print(f'Local_factor: {local}')
        self.get_secret(int(self.sock.recv(1024)))
        self.sock.send(bytes(f'{local}', encoding="UTF-8"))


class Server(Connect):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.output = None

    def start(self):
        self.thd = Thread(target=self.communicate)
        self.thd.start()

    def communicate(self):
        self.conn, self.addr = self.sock.accept()
        self.get_prime(int(self.conn.recv(1024)))
        self.get_base(int(self.conn.recv(1024)))
        local = self.generate_local_secret()
        print(f'Local_factor: {local}')
        self.conn.send(bytes(f"{local}", encoding="UTF-8"))
        self.get_secret(int(self.conn.recv(1024)))


#

server = Server(host='localhost', port=11601)
client = Client(host='localhost', port=11601)

for proc in [server, client]:
    proc.start()

for proc in [server, client]:
    proc.thd.join()

print(server.prime, server.base)
print(client.prime, client.base)
