from ipaddress import ip_network

net = ip_network('191.89.109.206/255.255.224.0', 0)
sum_octets = sum(int(part) for part in str(net[-2]).split('.'))
print(sum_octets)