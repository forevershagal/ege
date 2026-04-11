#а - текущее число, b - целевое число,
# с - предыдущее команда, r - флаг наличия 6
def f(a, b, c=0, r=False):
    if a > b or a == 18:
        return 0
    if a == b and r:
        return 1
    if a == 6:
        r = True

    s = f(a*2, b, 2, r)
    if c!= 1:
        s += f(a*3, b, 3, r)
    if c!= 2:
        s += f(a+4, b, 1, r)
    return s

print(f(2, 296))