import nashpy as nash
import numpy as np

A = np.array([[0, -4, 2], [-2, 0, -4], [2, 4, 0]])

game = nash.Game(A)

print(game)

sigma_r = [2, 4, 0]
sigma_c = [-2, 0, -4]
game[sigma_r, sigma_c]

eqs = game.support_enumeration()
list(eqs)
