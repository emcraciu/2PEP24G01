import os
import re
import time

from modul2.app1 import get_interface_ip


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
        route_output = os.popen("route print").read()

        split_routes = re.split(r"Active\sRoutes:", route_output)
        for route_table in split_routes[1:]:
            for line in route_table.splitlines():
                routes = re.search(r"(?P<route>[0-9.]+\s+[0-9.]+\s+([0-9.]+|On-link)\s+[0-9.]+\s+\d{1,3})", line)
                if routes:
                    print(routes.group("route"))


system = SystemInformation()
system.get_route_information()
