alf = 'ЁКЖИ'
c = 0
for i in alf:
    for g in alf:
        for h in alf:
            for j in alf:
                c += 1
                s = i+g+h+j
                if s == 'ЁЖИК':
                    print(c)