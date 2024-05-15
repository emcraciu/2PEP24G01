# import time
# from multiprocessing import Process
#
#
# def f(name):
#     print('hello', name)
#     time.sleep(5)
#     print('hello again', name)
#
#
# if __name__ == '__main__':
#     processes = []
#     for name in ['bob', 'alice']:
#         p = Process(target=f, args=(name,))
#         p.start()
#         processes.append(p)
#     print("after start")
#     for process in processes:
#         process.join()
import json
from multiprocessing import Pool
import requests


def time_zone(region):
    print(f"Process region: {region}")
    # response = requests.get(f'https://worldtimeapi.org/api/timezone/{region}')
    response = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={region}")
    text = response.text
    time_zones = json.loads(text)
    return time_zones  # needs to be python builtin object


if __name__ == '__main__':
    with Pool(5) as p:
        result = p.map(time_zone, ["Africa/Juba", "America/Caracas", "Europe/Amsterdam"])
        print(result)
