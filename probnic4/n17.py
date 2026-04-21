f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/17__a7wt8.txt')
a = [int(i) for i in f]
max28 = max([x for x in a if abs(x) % 100 == 28])
ans = []
for i in range(len(a)-2):
    triple = a[i:i+3]
    has_three_digit = any(100 <= abs(x) <= 999 for x in triple)
    avg = sum(triple) / 3
    avg_positive = avg > 0
    avg_less_than_max28 = avg < max28
    if has_three_digit and avg_positive and avg_less_than_max28:
        ans.append(sum(triple))
print(len(ans), max(ans))
