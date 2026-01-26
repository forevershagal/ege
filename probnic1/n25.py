import math
cnt = 0
ans = []
for x in range(316312, 451245):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)
        d = math.prod(c)
        if d % 14 == 0:
            ans += [d]
print(len(ans), sum(map(int, str(max(ans)))))



