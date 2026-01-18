alf = 'ЛОКН'
c = 0
for i in alf:
    for g in alf:
        for h in alf:
            for k in alf:
                c += 1
                s = i+g+h+k
                if s == 'КЛОН':
                    print(c)