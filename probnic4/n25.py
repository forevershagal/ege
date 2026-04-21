def f(x):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)
    return c
cnt = 0
for n in range(8996453, 10000000):
    d = f(n)
    if len(d) == 1 or len(d) == 2:
        if all(str(n).count('3') == 2 for n in d):
            print(n, max(d))
            cnt += 1
            if cnt == 5:
                break
