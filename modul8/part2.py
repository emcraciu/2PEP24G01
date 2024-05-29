# import random
# from threading import Thread, RLock
#
#
# def rand_sleep(lock: RLock):
#     t = random.randint(1, 5)
#     print(f"Sleep: {t}")
#     lock.acquire()  # first lock
#     try:
#         if t == 3:
#             raise ValueError("Cannot do 3s sleep")
#     finally:
#         lock.acquire(timeout=10)  # second lock
#         lock.release()  # release second lock
#         lock.release()  # release first lock
#     print("Function complete")
#
#
# process_lock = RLock()
# processes = []
# for _ in range(5):
#     thd = Thread(target=rand_sleep, args=(process_lock,))
#     thd.start()
#     processes.append(thd)
#
# for process in processes:
#     process.join()


import random
from threading import Thread, RLock


def rand_sleep(lock: RLock):
    t = random.randint(1, 5)
    print(f"Sleep: {t}")
    lock.acquire()  # first lock
    try:
        if t == 3:
            rand_sleep(lock)
            print("End reacquired lock")
    finally:
        lock.release()  # release first lock
    print("Function complete")


process_lock = RLock()
processes = []
for _ in range(5):
    thd = Thread(target=rand_sleep, args=(process_lock,))
    thd.start()
    processes.append(thd)

for process in processes:
    process.join()
