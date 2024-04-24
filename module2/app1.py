config = """

Windows IP Configuration


Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2001:470::
   Temporary IPv6 Address. . . . . . : 2001:470::
   Link-local IPv6 Address . . . . . : fe80::c90d:6547:1c91:e141%16
   IPv4 Address. . . . . . . . . . . : 192.168.1.10
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::7a9a:18ff:fe8c:7977%16
                                       192.168.1.1

Wireless LAN adapter Wi-Fi:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter vEthernet (Default Switch):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::3cae:7bff:dcd1:e9e8%41
   IPv4 Address. . . . . . . . . . . : 172.31.112.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :

Ethernet adapter vEthernet (Default Switch (Ethernet)):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::af08:ea1d:4149:7fd2%49
   IPv4 Address. . . . . . . . . . . : 172.17.0.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :

Ethernet adapter vEthernet (Default Switch (Wi-Fi)):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::7db5:ba5a:ab3e:b263%56
   IPv4 Address. . . . . . . . . . . : 172.29.96.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
"""

# get interface as key in dict and IP / subnet as value
{"Ethernet adapter vEthernet (Default Switch (Wi-Fi))": "172.29.96.1/255.255.240.0" }

def get_interface_ip(ipconfig_output) -> dict:
    pass