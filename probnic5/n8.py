import itertools

count = 0
for p in itertools.product('ГРОЗА', repeat=7):
    if p.count('З') >= 2:
        count += 1
print(count)