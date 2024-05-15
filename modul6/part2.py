import json
from multiprocessing import Process, Queue
import requests


def time_zone1(queue: Queue):
    region = queue.get(timeout=10)
    print(f"Process region: {region} {__name__}")
    response = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={region}")
    text = response.text
    time_zones = json.loads(text)
    return time_zones  # needs to be python builtin object

def time_zone2(queue: Queue):
    region = queue.get(timeout=10)
    print(f"Process region: {region} {__name__}")
    response = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={region}")
    text = response.text
    time_zones = json.loads(text)
    return time_zones  # needs to be python builtin object


if __name__ == '__main__':
    q = Queue()
    for region in ["Africa/Juba", "America/Caracas", "Europe/Amsterdam"]:
        q.put(region)

    for _ in range(4):
        p = Process(target=time_zone1, args=(q,))
        p.start()
        p = Process(target=time_zone2, args=(q,))
        p.start()
