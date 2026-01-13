# ------------------------------ 1 куча ------------------

# lru_cache позволит сэкономить ресурсы компьютера.
# Функция будет сохранять прошлые значения функций, а значит не придётся считать из заново.
from functools import lru_cache
@lru_cache(None)
def game(first_heap): # Функция игры
    if first_heap >= 39: # Если камней в куче стало больше 38
        return 0 # прекращаем игру
    moves = [game(first_heap+1),game(first_heap+2),game(first_heap*2)] # Прописываем ходы возможные в партии
    petya_win = [i for i in moves if i <= 0]
    if petya_win: # Проверяем, есть ли выигрыш Пети в данной позиции
        return -max(petya_win) + 1
    else: # Если в данной позиции выигрыш Вани
        return -max(moves)

for i in range(1,38):
    if game(i) == 1: # Если в данной позиции Петя побеждает первым ходом
        print(i)