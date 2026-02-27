for x in '0123456789ABCDEFGHIJKLNMOPQ':
    s = int('2F'+x+'L325', 27) + int('17' + x + 'BC5', 27) + int('31' + x + 'MN', 27)
    if s % 15 == 0:
        print(x, s // 15)
        break