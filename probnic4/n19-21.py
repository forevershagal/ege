from functools import lru_cache

@lru_cache(maxsize=None)
def f(heap):
    if heap >= 124:
        return 0
    moves = [f(heap+1), f(heap+5), f(heap*3)]
    petya_win = [i for i in moves if i <= 0]
    if petya_win:
        return -max(petya_win)+1
    else:
        return -max(moves)

for i in range(1, 124):
    if f(i) == -1 and f(i) != 1:
        print(i)