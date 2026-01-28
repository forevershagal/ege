# Для узла с IP-адресом 7.120.112.5 адрес сети равен 7.120.96.0.
# Чему равен номер компьютера в этой сети?
# Ответ запишите в виде десятичного числа.

from ipaddress import *

# for i in range(32):
#     net = ip_network('7.120.112.5/' + str(i), 0)
#     print(net, net.netmask)

# Вывод: 7.120.96.0/19 255.255.224.0
# Нам нужен /19

net = ip_network('7.120.96.0/19', 0)
ip = ip_address('7.120.112.5')
nm = int(ip) - int(net.network_address)
print(nm)