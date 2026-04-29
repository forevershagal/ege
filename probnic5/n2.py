print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((not x <= y) == (y == (not z))) and (not w)
                # В условии выражение: ((not x) -> y) and (y == (not z)) and (not w)
                f = ((not(not x) or y) and (y == (not z)) and (not w))
                if f:
                    print(x, y, z, w)
# Сопоставив вывод с фрагментом из условия, получаем порядок переменных.