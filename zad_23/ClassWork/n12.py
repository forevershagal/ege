res = set()

def f(a, c, c1, c2):
    if c == 11:
        res.add(a)
        return
    if c1 < 2 and c2 < 2:
        f(a+2, c+1, c1+1, 0)
        f(a*2, c+1, 0, c2+1)
    elif c1 < 2:
        f(a+2, c+1, c1+1, 0)
    else:
        f(a*2, c+1, 0, c2+1)
f(1, 0, 0, 0)
print(len(res))
