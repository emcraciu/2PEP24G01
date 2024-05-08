# get route from os using subprocess
import subprocess

output_route = subprocess.Popen(["route", "print", "-4"], stdout=subprocess.PIPE)

result = output_route.communicate(timeout=5)
print(result)