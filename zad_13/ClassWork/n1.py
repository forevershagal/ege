from ipaddress import *

net = ip_network('68.232.57.148/255.255.252.0', 0)
print(bin(int(net.network_address))[2:].zfill(32).count('0'))