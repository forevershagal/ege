cnt = 0
for x in range(3, 30002):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)
    if all(i % 2 == 0 or i % 3 == 0 for i in c) and len(c) == 6:
        cnt += 1
print(cnt)