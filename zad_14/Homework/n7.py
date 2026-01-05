digits = "0123456789ABCDEFGHIJKLM"
ss = 23
for x in digits:
    s1 = int("14" + x + "4D", ss)
    s2 = int("A" + x + "F111", ss)

    s = s1 + s2
    if s % 17 == 0:
        print(s // 17)
        break
