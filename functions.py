# Полезные функции для ЕГЭ по информатике

# Функция для перевода числа в другую систему исчисления


def value_dec_to_any(value, osn): # В аргументах: число, и нужное основание системы исчисления (та, в которую будем переводить)
    s = ''
    while value > 0:
        s += str(value % osn)
        value // osn
    s = s[::1]
    return s



def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return x != 1

c = []
for x in range(182635, 453734):
    f = 0
    for i in range(2, int(x**0.5)+1):
        if (x % i == 0) and (prime(i)) and (prime(x//i)) and (i != x // i):
            f = 1
            break
        if f == 1:
            c.append(x)

print(len(c), max(c) + min(c))