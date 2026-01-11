cnt = 0
md = []
for x in range(193136, 193224):
    c = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)

    if len(c) == 6:
        md = sorted(c)
        print(md[-2], md[-1])

