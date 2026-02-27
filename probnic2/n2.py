print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((y <= x) or (not(z) and w)) == (w == x)):
                    print(w, x, y, z)