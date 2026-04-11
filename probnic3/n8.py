from itertools import product

l = 'ЕПРЮ'
cnt = 0
for x in product(l, repeat=5):
    s = ''.join(x)
    cnt += 1
    if 'ЮР' in s:
        print(cnt, s)