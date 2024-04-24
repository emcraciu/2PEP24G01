import os
import re
import time

from module2.app1 import get_interface_ip


class SystemInformation():

    def get_interface_ips(self):
        ip_data = os.popen('ipconfig').read()
        return get_interface_ip(ip_data)

    def get_cpu_average(self, interval):
        start_time = time.time()
        total = 0
        count = 0
        while time.time() <= start_time + interval:
            cpu_usage_output = os.popen('wmic cpu get loadpercentage')
            pattern = re.compile(r"(?P<cpu>\d{1,3})")
            cpu_group = pattern.search(cpu_usage_output.read())
            number = int(cpu_group.group('cpu'))
            total += number
            count += 1
        average = total / count
        return average

    def get_route_information(self):
        pass


system = SystemInformation()
print(system.get_cpu_average(7))
