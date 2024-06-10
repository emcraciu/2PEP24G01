"""
get timezones
"""

import json

import requests


def time_getter(url: str = "https://www.timeapi.io/api/TimeZone/AvailableTimeZones"):
    """
    function to get timezones
    :return:
    """
    result = []
    response = requests.get(
        url,
        timeout=10,
    )
    text = response.text
    try:
        for obj in json.loads(text):
            result.append(obj)
    except Exception:
        return []
    return result


if __name__ == "__main__":
    print(time_getter("http://example.com"))
