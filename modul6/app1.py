# get datetime object from "https://www.timeapi.io/api/Time/current/zone?timeZone=..."

def time_zone(region):
    time_zones = None
    return time_zones  # needs to be python builtin object


if __name__ == '__main__':
    with Pool(5) as p:
        result = p.map(time_zone, ["Africa/Juba", "America/Caracas", "Europe/Amsterdam"])
        print(result)