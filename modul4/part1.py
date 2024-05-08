import subprocess


# result = subprocess.run(['ipconfig'])
# # shell True required for build in commands
# result = subprocess.run(['dir'], shell=True)
# # with arguments
# result = subprocess.run(["route", "print", "-6"])

result = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE)
output = result.communicate(timeout=10)
print(output)

# file path is relative to working directory
result = subprocess.Popen(['notepad', 'file.txt'], stdout=subprocess.PIPE)
output = result.communicate(timeout=10)
print(output)