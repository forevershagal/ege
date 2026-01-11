cnt = 0
for x in range(100100, 300101):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)
        if len(c) > 6:
            break
    if len(c) == 4:
        cnt += 1

print(cnt)