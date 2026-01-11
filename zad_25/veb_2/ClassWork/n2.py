cnt = 0
for x in range(100010, 321342):
    if x**0.5 == int(x**0.5):
        c = set()
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                c.add(x)
                c.add(x//i)

            if len(c) > 3:
                break

        if len(c) == 3:
            cnt += 1

print(cnt)