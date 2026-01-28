from ipaddress import *

net = ip_network('15.58.216.208/255.255.255.128', 0)
c = 0
for i in net.hosts():
    adr = bin(int(i))[2:].zfill(32)
    if adr.count('0') > 12:
        c += 1
print(c)