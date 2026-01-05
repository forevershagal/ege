f = open('D:/INC/task17_veb1_class/2.csv')
c = 0

for i in f:

    a = sorted(map(int, i.split(',')))

    # Список чисел, встречающихся ровно 2 раза
    c2 = [j for j in a if a.count(j) == 2]

    # Список чисел, встречающихся ровно 1 раз
    c1 = [g for g in a if a.count(g) == 1]

    # Если 2 повторяющихся числа, 3 неповторяющихся
    # и среднее арифметическое с2 < среднего арифм всех чисел
    if (len(c2) == 4) and (len(c1) == 3) and ((sum(c2) / 4) < (sum(a) / 7)):
        c += 1

print(c)