from itertools import product
c = 0
for x in product('БУРЖАЗИЯ', repeat=8):
    s = "".join(x)
    if "БУРЖУИ" not in s:
        c += 1

print(c)