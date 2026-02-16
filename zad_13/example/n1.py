from ipaddress import *


# Дан айпи адрес узла и маска сети найти количество нулей в двоичной записи адреса сети
net = ip_network('68.232.57.148/255.255.252.0', 0)

res = net.network_address
print(bin(int(res))[2:].zfill(32).count('0'))