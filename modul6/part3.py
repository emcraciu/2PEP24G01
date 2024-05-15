import json
from multiprocessing import Process, Queue
import requests


def time_zone_generator(queue: Queue):
    for region in ["Africa/Juba", "America/Caracas", "Europe/Amsterdam"]:
        queue.put(region)

def time_zone_consumer(queue: Queue, out: Queue):
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
    processes = []
    for _ in range(2):
        p = Process(target=time_zone_consumer, args=(q, out))
        p.start()
        processes.append(p)
    p = Process(target=time_zone_generator, args=(q,))
    p.start()
    processes.append(p)

    for proc in processes:
        proc.join()
    while not out.empty():
        print(out.get())
