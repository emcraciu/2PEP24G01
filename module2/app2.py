import os
import re
from module2.app1 import get_interface_ip

class SystemInformation():

    def get_interface_ips(self):
        ip_data = os.popen('ipconfig').read()
        return get_interface_ip(ip_data)

    def get_cpu_average(self, interval):
        return average



