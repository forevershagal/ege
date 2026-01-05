f = open('D:/INC/task17_veb1_class/3.csv')
c = 0

for i in f:
    a = sorted(map(int, i.split(',')))

    # Создаем список последних цифр чисел
    c10 = [g%10 for g in a]

    # сумма четных чисел
    ch = sum(j for j in a if j % 2 == 0)

    # Если уникальных последних цифр 4 и сумма четных точек максимума
    if (len(set(c10))) == 4 and (ch > max(a)):
        c += 1

print(c)