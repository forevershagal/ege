alf = 'НРДО'
c = 0
for i in alf:
    for g in alf:
        for h in alf:
            for j in alf:
                s = i + g + h + j
                c += 1
                if s == 'ДРОН':
                    print(c)