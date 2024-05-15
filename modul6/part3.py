# import json
# from multiprocessing import Process, Queue
# import requests
#
#
# def time_zone_generator(queue: Queue):
#     for region in ["Africa/Juba", "America/Caracas", "Europe/Amsterdam"]:
#         queue.put(region)
#
# def time_zone_consumer(queue: Queue, out: Queue):
#     while True:
#         region = queue.get(timeout=10)
#         print(f"Process region: {region} {__name__}")
#         response = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={region}")
#         text = response.text
#         time_zones = json.loads(text)
#         out.put(time_zones)
#     # return time_zones  # needs to be python builtin object
#
#
# if __name__ == '__main__':
#     q = Queue()
#     out = Queue()
#     processes = []
#     for _ in range(2):
#         p = Process(target=time_zone_consumer, args=(q, out))
#         p.start()
#         processes.append(p)
#     p = Process(target=time_zone_generator, args=(q,))
#     p.start()
#     processes.append(p)
#
#     for proc in processes:
#         proc.join()
#     while not out.empty():
#         print(out.get())


import json
import time
from multiprocessing import Process, Lock
import requests


def time_zone_generator(lock: Lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        print(f"number is {i}")
        lock.release()
def time_zone_consumer(lock:Lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        try:
            print(f"number is {i}")
            raise Exception
        finally:
            lock.release()


if __name__ == '__main__':
    l = Lock()
    processes = []
    for _ in range(10):
        p = Process(target=time_zone_consumer, args=(l, ))
        p.start()
        processes.append(p)
        p = Process(target=time_zone_generator, args=(l,))
        p.start()
    processes.append(p)

    for proc in processes:
        proc.join()
