from typing import List
from itertools import product
import numpy as np
from scipy.optimize import linprog

number_choices: List[int] = [1, 2, 3]

# smaller than one looses
sto: int = 4
# smaller more than one
smto: int = -2
# equal to each other
eteo: int = 0

# 0 index me 1 index opponent
all_variants = list(product(number_choices, repeat=2))

matrix_choices: np.ndarray = np.zeros((len(number_choices), len(number_choices)), dtype=np.int32)

for index, choice in enumerate(np.nditer(matrix_choices, op_flags=['readwrite'])):
    # print(index, choice)
    if all_variants[index][0] - all_variants[index][1] == -1:
        choice[...] = sto
    elif all_variants[index][0] - all_variants[index][1] < -1:
        choice[...] = smto
    elif all_variants[index][0] == all_variants[index][1]:
        choice[...] = eteo
    elif all_variants[index][0] - all_variants[index][1] == 1:
        choice[...] = -sto
    elif all_variants[index][0] - all_variants[index][1] > 1:
        choice[...] = -smto

print("___INITIALIEZ___")
print(matrix_choices)
# print(matrix_choices)
print("IS NEGATIVE", (matrix_choices < 0).any())

if (matrix_choices < 0).any():
    matrix_choices = matrix_choices + np.max(matrix_choices)
    print("___AFTER ADDED___")
    print(matrix_choices)

print("____PREPARING CALCULATIONS____")
c = np.array([1 for i in number_choices])
print("MIN COEFF", c)
# print(matrix_choices.transpose())


print("_____COEFFICIENTS____")
A = np.array([-column for column in matrix_choices.transpose()])
print(A)
# x1 + x2 +x3... condtion
# print("BEFORE CONSTRAINT\n", A)
# A = np.append(A, np.array([[1, 1, 1]]), axis=0)
# print("AFTER CONSTRAINT\n", A)

b = np.array([-1 for value in number_choices])
print(b)
# x1 + x2 +x3... condtion
# print("BEFEORE B \n", b)
# b = np.append(b, np.array([[1]]))
# print("AFTER B", b)

#additional bounds
# bounds = [(-1, 0) for value in number_choices]
# res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)
print("ZISEEE", c.size)
ones_constraint = np.ones((len(number_choices), len(number_choices)))
ones_values = np.array([1 for i in number_choices])
res = linprog(c, A_ub=A, b_ub=b, A_eq=ones_constraint, b_eq=ones_values)
print(res)
