def game(heap):
    if heap >= 29:
        return 0
    moves = [game(heap+1), game(heap*2)]
    petya_win = [i for i in moves if i <= 0]
    if petya_win:
        return -max(petya_win)+1
    else:
        return -max(moves)

for i in range(1, 29):
    if (game(i) == - 1 or game(i) == -2) and game(i) != -1:
        print(i)