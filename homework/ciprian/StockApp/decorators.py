from functools import wraps
import time
import csv

def log_time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        new_row = [str(func.__name__), str(start), str(end), str(end-start)]
        with open(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\logfile.csv',
                  'a', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(new_row)
        return result

    return wrapper

