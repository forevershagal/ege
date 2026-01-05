for x in '0123456789A':
    s1 = '348' + x + '5'
    s2 = '1' + x + '111'
    s = int(s1) + int(s2)
    if s % 8 == 0:
        print(s // 8)