for n in range(12, 100):
    s = bin(n)[2:]
    digit2 = s[1]
    # Заменяем последнюю цифру на вторую дважды
    new_s = s[:-1] + digit2 + digit2
    r = int(new_s, 2)
    if r > 48:
        print(n)
        break