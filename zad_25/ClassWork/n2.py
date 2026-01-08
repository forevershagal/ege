def prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return x != 1

c = []

for x in range(182635, 453734):
    f = 0
    for i in range(2, int(x**0.5)+1):
        if (x % i == 0) and prime(i) and prime(x//i) and (i != x // i):
            f = 1
            break
    if f == 1:
        c.append(x)

print(len(c), max(c) + min(c))
