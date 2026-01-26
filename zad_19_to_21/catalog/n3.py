# Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней.
# Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может:
# убрать из кучи два камня,
# уменьшить количество камней в куче в три раза (количество камней,
# полученное при делении, округляется до меньшего).
# Игра завершается в тот момент, когда суммарное количество камней в кучах становится не более 165.
# Победителем считается игрок, сделавший последний ход,
# т.е.первым получивший суммарно в кучах 165 камней или меньше.
# В начальный момент в первой куче было 17 камней, во второй куче – S камней; S > 149.
# Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
# Укажите максимальное значение S, при котором Ваня может выиграть за один ход при неудачном ходе Пети.


from functools import lru_cache

@lru_cache(None)
def game(first_heap, second_heap, cnt=0):
    if first_heap + second_heap <= 165:
        return 0

    if cnt > 6:
        return 10 ** 10

    moves = []

    if first_heap - 2 > 0:
        moves.append(game(first_heap - 2, second_heap, cnt + 1))
    if second_heap - 2 > 0:
        moves.append(game(first_heap, second_heap - 2, cnt + 1))
    if first_heap > 0:
        moves.append(game(first_heap // 3, second_heap, cnt + 1))
    if second_heap > 0:
        moves.append(game(first_heap, second_heap // 3, cnt + 1))

    petya_win = [i for i in moves if i <= 0]
    if petya_win:
        return -max(petya_win)+1
    else:
        return -max(moves)

for i in range(150, 1500):
    if (game(17, i-2, 0) == 1 or
            game(17, i // 3, 0) == 1 or
            game(17-2, i, 0) == 1 or
            game(17 // 3, i, 0) == 1):
        print(i)
