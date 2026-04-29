from functools import lru_cache


@lru_cache(None)
def game(a, b):
    if a + b <= 40:
        return 0
    moves = []
    if a > 0:
        moves.append(game(a-1, b))
    if a > 1:
        if a % 2 == 0:
            moves.append(game(int(a//2), b))
        else:
            moves.append(game(int(a//2)+1, b))
    if b > 0:
        moves.append(game(a, b-1))
    if b > 1:
        if b % 2 == 0:
            moves.append(game(a, int(b//2)))
        else:
            moves.append(game(a, int(b//2)+1))
    petya_win = [i for i in moves if i <= 0]
    if petya_win:
        return -max(petya_win)+1
    else:
        return -max(moves)

for i in range(20, 200):
    if game(20, i) == -2:
        print(i)