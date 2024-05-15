import json
from multiprocessing import Process, Queue, Lock
import requests


def time_zone_generator(queue: Queue):
    response = requests.get('https://www.timeapi.io/api/TimeZone/AvailableTimeZones')
    text = response.text
    queue.put(json.loads(text))


def time_zone_consumer(queue: Queue, out: Queue, lock_: Lock):
    while True:
        region = queue.get(timeout=10)
        print(f"Process region: {region} {__name__}")
        response = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={region}")
        text = response.text
        time_zones = json.loads(text)
        out.put(time_zones)
    # return time_zones  # needs to be python builtin object


if __name__ == '__main__':
    q = Queue()
    out = Queue()
    l = Lock()
    processes = []
    for _ in range(100):
        p = Process(target=time_zone_consumer, args=(q, out, l))
        p.start()
        processes.append(p)
    p = Process(target=time_zone_generator, args=(q,))
    p.start()
    processes.append(p)

    for proc in processes:
        proc.join()
    while not out.empty():
        print(out.get())
