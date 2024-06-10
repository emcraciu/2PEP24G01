import time
import datetime as dt
from functools import wraps

class ConvertTime:
    def __init__(self):
        self.current_time = time.time()

    def get_time(self):
        time_now = self.current_time
        return time.strftime('%Y.%m.%d-%I:%M:%S %p', time.localtime(time_now))

    def set_time(self, user_time):
        new_time = dt.datetime.strptime(user_time, '%Y.%m.%d-%I:%M:%S %p').timetuple()
        self.current_time = time.mktime(new_time)

def convert_to_24h(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_to_format = func(*args, **kwargs)
        return dt.datetime.strptime(time_to_format, '%Y.%m.%d-%I:%M:%S %p')
    return wrapper

@convert_to_24h
def time_in_24h(time_to_format):
    return time_to_format

ttime = ConvertTime()

print(f'Time now in AM/PM format: {ttime.get_time()}')
print(f'Time now in 24h format: {time_in_24h(ttime.get_time())}\n')

ttime.set_time('2023.10.30-03:54:30 PM')
user_time = ttime.get_time()

print(f'User time in AM/PM format: {user_time}')
print(f'User time in 24h format: {time_in_24h(user_time)}\n')

user_time1 = '2025.10.30-11:54:30 PM'

print(f'User time 1 in AM/PM format: {user_time1}')
print(f'User time 1 in 24h format: {time_in_24h(user_time1)}')