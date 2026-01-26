# Задача. Гоша составляет восьмизначные числа.
# Причём рядом не должны стоять цифры с одинаковым остатком от деления на 5,
# а также на последнем месте может быть только чётная цифра.
# Сколько чисел может составить Гоша?


def count_numbers():
    digits_by_rem = {
        0: [0, 5],
        1: [1, 6],
        2: [2, 7],
        3: [3, 8],
        4: [4, 9],
    }

    first_counts = [0]*5

    for rem in range(5):
        count = 0
        for i in digits_by_rem[rem]:
            if i != 0:
                count += 1

        first_counts[rem] = count

    mid_counts = [len(digits_by_rem[rem]) for rem in range(5)]
    last_counts = [0]*5

    for rem in range(5):
        for i in digits_by_rem[rem]:
            if i % 2 == 0:
                count += 1

        last_counts[rem] = count

    dp = [first_counts[:]]

    for pos in range(1, 7):
        new_dp = [0]*5
        for prev_rem in range(5):
            if dp[pos-1][prev_rem] == 0:
                continue

            for new_rem in range(5):
                if new_rem == prev_rem:
                    continue

                new_dp[new_rem] += dp[pos-1][prev_rem] * mid_counts[new_rem]

        dp.append(new_dp)

    total = 0

    for prev_rem in range(5):
        if dp[6][prev_rem] == 0:
            continue

        for last_rem in range(5):
            if last_rem == prev_rem:
                continue

            total += dp[6][prev_rem] * last_counts[last_rem]
    return total

result = count_numbers()
print(result)

