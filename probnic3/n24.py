from re import *

f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/probnic/24_1__6ba37.txt').readline()
# регулярка числа
s = r"(0|[1-6][0-6]*)"
# регулярка выражения
vr = rf"{s}([+*]{s})*"
m = max([i.group() for i in finditer(vr, f)], key=len)
print(len(m))