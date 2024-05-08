## create class for system monitor with Popen

import re
import subprocess
from typing import Union


class Utils:

    def cpu_usage(self) -> int:
        cmd = ['wmic', 'cpu', 'get', 'loadpercentage']
        process = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE)
        result = process.communicate(timeout=10)
        result_fin = re.compile(r'(\d{1,3})')
        return int(result_fin.search(result[0]).group(0))

    def get_ip_address(self, interface_idx: Union[str, int]) -> str:
        cmd_ip = ["powershell", "-Command", "Get-NetIPAddress", "-InterfaceIndex", str(interface_idx)]
        ip_address = subprocess.Popen(cmd_ip, text=True, stdout=subprocess.PIPE)
        result_ip = ip_address.communicate(timeout=4)[0]
        print(result_ip)
        pattern = re.compile(r"IPAddress\s+:\s+(\d+\.\d+\.\d+\.\d+|[0-9a-f:]+)")
        return str(pattern.findall(result_ip)).strip("[]")


if __name__ == "__main__":
    util = Utils()
    result = util.cpu_usage()
    print(f'cpu usage: {result}')
    util.get_ip_address(1)
    print(f'ip address: {result}')
