print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((w or not(x)) and (w == (not(y))) and (w <= z)) == 1:
                    print(w, x, y, z)

# Ответ: wyzx