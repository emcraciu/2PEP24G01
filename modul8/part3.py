# race functions
import random
import threading
import time
from threading import Thread, Event, Barrier


# time to prepare
# all functions must start at the same time

def runner(e: Event, b: Barrier):
    print("Getting ready")
    time.sleep(random.randint(3, 5))
    b.wait()
    print(f"Runner: {threading.get_native_id()} is ready")
    e.wait()
    run_time = random.randint(1, 50)/10
    print(f"Running for {run_time}")
    time.sleep(run_time)
    if e.is_set():
        print(f"Runner {threading.get_native_id()} failed the race")
    else:
        e.set()
        print(f"Runner {threading.get_native_id()} is the winner")



def referee(e: Event, b: Barrier):
    time.sleep(random.randint(1, 2))
    b.wait()
    print(f"Referee: {threading.get_native_id()} is ready")
    print("Start")
    e.set()
    time.sleep(1)
    e.clear()


event = Event()
barrier = Barrier(11)
processes = []
for _ in range(1):
    thd = Thread(target=referee, args=(event, barrier))
    processes.append(thd)

for _ in range(10):
    thd = Thread(target=runner, args=(event, barrier))
    processes.append(thd)

for thd in processes:
    thd.start()
