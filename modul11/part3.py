"""
get timezones
"""

import json

import requests

from modul1.app3 import test_cond


# class Json:
#     def loads(self, test_to_load):
#         return ["My str"]
#
#
# json = Json()


def time_getter(url: str = "https://www.timeapi.io/api/TimeZone/AvailableTimeZones"):
    """
    function to get timezones
    :return:
    """
    response = requests.get(url, timeout=10)
    text = response.text
    if test_cond:
        return json.loads(text)
    else:
        return None


if __name__ == "__main__":
    print(time_getter())
