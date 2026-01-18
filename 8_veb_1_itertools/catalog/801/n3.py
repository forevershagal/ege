alf = 'БАКРД'
c = 0
for i in alf:
    for g in alf:
        for h in alf:
            for j in alf:
                for k in alf:
                    for l in alf:
                        c += 1
                        s = i+g+h+j+k+l
                        if s == 'БАРДАК':
                            print(c)

