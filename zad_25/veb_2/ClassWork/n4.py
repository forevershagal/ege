def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False

    return x > 1

l = []

for x in range(264871, 322990):
    f = 0
    for i in range(2, int(x**0.5)+1):
        if (x % i == 0) and (i % 10 == (x//i) % 10) and (prime(i)) and (prime(x//i)) and (i != x // i):
            f = 1
            break

    if f == 1:
        l.append(x)

print(len(l), int(sum(l) / len(l)))