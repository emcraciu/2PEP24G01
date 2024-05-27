import random
from threading import Thread, Lock

def rand_sleep(lock: Lock):
    t = random.randint(1, 5)
    print(f"Sleep: {t}")
    lock.acquire()
    try:
        if t == 3:
            raise ValueError("Cannot do 3s sleep")
    finally:
        lock.acquire(timeout=10)
        lock.release()
    print("Function complete")




process_lock = Lock()
processes = []
for _ in range(5):
    thd = Thread(target=rand_sleep, args=(process_lock,))
    thd.start()
    processes.append(thd)

for process in processes:
    process.join()

