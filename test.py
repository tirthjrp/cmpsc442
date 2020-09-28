import homework3_cmpsc442
import homework2_tpp5217
import time
b = [[False] * 3 for i in range(3)]
g = homework3_cmpsc442.DominoesGame(b)
g.perform_move(0, 1, True)
print(g.get_best_move(False, 1))