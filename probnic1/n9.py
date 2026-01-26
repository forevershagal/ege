f = open('D:/INF_tasks/probnic1/6__3yr40.csv')

count = 0


a = [list(map(int, i.replace(',', ' ').split())) for i in f]

for g in a:
    odd_sum = sum([x for x in g if x % 2 != 0])
    less_than_50 = sum([1 for x in g if x < 50])
    greater_than_50 = sum([1 for x in g if x > 50])
    if odd_sum % 7 == 0 or less_than_50 > greater_than_50:
        count += 1

print(count)