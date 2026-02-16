from ipaddress import *

# Дан адрес узла и маска сети найти полный адрес сети без точек

net = ip_network('31.221.163.10/255.255.240.0', 0)
res = net.network_address
print(res)