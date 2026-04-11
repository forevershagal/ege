print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(x <= y) or z or not(w)) == False:
                    print(w, x, y, z)