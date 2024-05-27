"""Create app that reads multiple time zones in thread and writes output to file
https://www.timeapi.io/api/Time/current/zone?timeZone=...
need to use Lock to write to file
"""

from time import sleep
import requests
import json
from threading import Thread, Lock


class TimeZoneWriter:
    time_zones = None

    def get_time_zones(self):
        res = requests.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones")
        text = res.text
        all_regions = json.loads(text)
        self.time_zones = all_regions

    def write_time_zone_data(self, data_lock: Lock):
        res = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={self.time_zones.pop()}")
        text = res.text
        zone_data = json.loads(text)
        data_lock.acquire()
        try:
            with open("time_zones.log", "a") as file:
                file.write(zone_data["dateTime"] + "\n")
                sleep(1)
                file.write(zone_data["date"] + "\n")
        finally:
            data_lock.release()


t = TimeZoneWriter()
lock = Lock()
t.get_time_zones()
for _ in range(len(t.time_zones[:5])):
    thd = Thread(target=t.write_time_zone_data, args=(lock,))
    thd.start()
