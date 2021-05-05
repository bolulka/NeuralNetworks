"""
Задание 3.  (из темы 4.2, тест 4):

Построить и обучить нейронные сети с одним и двумя скрытыми
слоями для распознавания прописных букв русского алфавита. В
качестве входных данных использовать свои инициалы (ФИО).
"""

import numpy as np


def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))


X = np.array([[1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0,
               1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
              [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1,
               1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1]])

y = np.array([[1, 0],
              [0, 1]])

np.random.seed(1)

syn0 = 2 * np.random.random((56, 10)) - 1
syn1 = 2 * np.random.random((10, 24)) - 1
syn2 = 2 * np.random.random((24, 2)) - 1

for j in range(100000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))

    l3_error = y - l3
    l3_delta = l3_error * nonlin(l3, True)

    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * nonlin(l2, True)

    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print('обучение на входных данных(Б, Ю, Ю):')
for el in l3:
    for el1 in el:
        print(int(el1 * 100), '%', sep='', end=' ')
    print()
print()

print('поврежденная буква Б:')
damaged_letter_B = np.array(
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0,
     0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0])
res_b = nonlin(np.dot(nonlin(np.dot(nonlin(np.dot(damaged_letter_B, syn0)), syn1)), syn2))
print(round(res_b[0] * 100, 2), '%', sep='', end=' ')
print(round(res_b[1] * 100, 2), '%', sep='', end=' ')
print()

print('поврежденная буква Ю:')
damaged_letter_Y = np.array(
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1,
     1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1])
res_y = nonlin(np.dot(nonlin(np.dot(nonlin(np.dot(damaged_letter_Y, syn0)), syn1)), syn2))
print(round(res_y[0] * 100, 2), '%', sep='', end=' ')
print(round(res_y[1] * 100, 2), '%', sep='', end=' ')
print()
