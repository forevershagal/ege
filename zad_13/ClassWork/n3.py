from ipaddress import *

net = ip_network('113.116.181.173/255.255.255.128', 0)
c = 0
for i in net:
    adr = bin(int(i))[2:].zfill(32)
    adr_end = adr[-4:]
    if adr_end in ['0000', '1111']:
        c += 1
print(c)
