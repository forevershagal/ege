for x in range(500001, 10**6):
    s = 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            s += i + (x // i)
            break

    if s % 10 == 6:
        print(x, s)

        ## неверно, посмотреть позже в чем ошибка!!!