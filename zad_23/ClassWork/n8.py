def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    o1 = f(a-3, b)
    o2 = o3 = 0
    if a%3 == 0:
        o2 = f(a//3, b)
    if a%2 == 0:
        o3 = f(a//2, b)
    return o1 + o2 + o3
print(f(30, 3))