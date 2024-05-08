# subprocess context
import time
from subprocess import Popen, PIPE

# with Popen(["python", "example.py"], stdout=PIPE, stdin=PIPE) as proc:
#     # time.sleep(1)
#     # print(proc.stdout.read())
#     # time.sleep(1)
#
#     proc.stdin.write(b"yes\n")
#     print(proc.stdout.read())