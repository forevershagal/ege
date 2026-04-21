print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not (not x or (z) or (w))) or (x and not z and y):
                    print(w, x, y, z)