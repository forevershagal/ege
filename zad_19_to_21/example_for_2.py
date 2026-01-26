# ----------------------- 2 кучи ---------------------
# lru_cache кэширует уже известные данные, ускоряя работу
from functools import lru_cache
@lru_cache(None)
def game(first_heap, second_heap, count_moves): # Функция игры.
    # count_moves - счётчик ходов в партии, его мы добавили для того,
    # чтобы избежать ошибки превышения лимита рекурсии.
    # Это работает следующим образом: если в партии больше 6 ходов, а партия не завершена,
    # то такая партия нам не подходит, поскольку в задачах у нас просят значения,
    # при которых Ваня или Петя побеждают максимум третьим ходом.
    if first_heap * second_heap >= 2048: # Если произведение камней в кучах стало больше 2047
        return 0 # Прекращаем игру
    if count_moves > 6: # Если в игре больше 6 ходов
        return 10**10 # Прерываем игру
    # Генерация всех возможных ходов
    moves = [game(first_heap, second_heap+1,count_moves+1), game(first_heap+1, second_heap,count_moves+1),
             game(first_heap * 2, second_heap,count_moves+1),game(first_heap, second_heap * 2,count_moves+1)]
    petya_win = [i for i in moves if i <= 0]
    if petya_win: # Если в данной позиции есть выигрыш Пети
        return -max(petya_win) + 1
    else: # Если в данной позиции выигрыш Вани
        return -max(moves)


for i in range(1,187):
    # Если в данной позиции возможен выигрыш Вани первым ходом
    if game(11,i,0) == -1:
        print(i)
        break



# from functools import lru_cache
#
# @lru_cache(None)
# def game(first, second, cnt=0):
#     if first * second >= 2048:
#         return 0
#
#     if cnt > 6:
#         return 10 ** 10
#
#     moves = [game(first, second+1, cnt + 1), game(first+1, second, cnt + 1),
#              game(first*2, second, cnt+1), game(first, second*2, cnt+1)]
#     petya_win = [i for i in moves if i <= 0]
#     if petya_win:
#         return -max(petya_win)+1
#     else:
#         return -max(moves)
#
#
# for i in range(1, 187):
#     if game(11, i, 0) == -1:
#         print(i)
