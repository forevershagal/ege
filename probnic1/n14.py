def f(n, osn):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s += str(n % osn)
        n = n // osn
    s = s[::-1]
    return s
mx_a = 0
ans = []

for x in range(2, 2026):
    m = 5**2025 + 5**200 -x
    a = f(m, 5)
    if a.count('4') >= mx_a:
        mx_a = a.count('4')
        ans.append(x)
print(max(ans))