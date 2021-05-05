"""
Задание 2.  (из  темы  4.2, тест 2):

С помощью нейронной сети на основе анализа набора характеристик, непонятно как влияющих на отнесение к классам,
произвести классификацию транспортных средств по классам: Легковой автомобиль; Пассажирский транспорт; Грузовой транспорт.

За основу взять следующие характеристики:
0) Большая снаряженная масса,
1) Большая мощность двигателя,
2) Большая пассажировместимость,
3) Большая грузоподъёмность.
"""

import numpy as np


def result(list):
    l = np.round(list)
    if l[0] == 1.:
        return 'легковой автомобиль'
    if l[1] == 1.:
        return 'пассажирский автобус'
    if l[2] == 1.:
        return 'грузовой транспорт'
    else:
        return 'не определено'


def normalize(n, x):
    if n == 0:
        if x < 0.5:
            return 0
        if x >= 0.5 and x < 1:
            return 0.25
        if x >= 1 and x < 2:
            return 0.5
        if x >= 2 and x < 5:
            return 0.75
        if x >= 5:
            return 1
    if n == 1:
        if x < 20:
            return 0
        if x >= 20 and x < 50:
            return 0.25
        if x >= 50 and x < 100:
            return 0.5
        if x >= 100 and x < 200:
            return 0.75
        if x >= 200:
            return 1
    if n == 2:
        if x < 2:
            return 0
        if x >= 2 and x < 5:
            return 0.25
        if x >= 5 and x < 10:
            return 0.5
        if x >= 10 and x < 20:
            return 0.75
        if x >= 20:
            return 1
    if n == 3:
        if x <= 1:
            return 0
        if x > 1 and x <= 2:
            return 0.25
        if x > 2 and x <= 3:
            return 0.5
        if x > 3 and x <= 4:
            return 0.75
        if x > 4:
            return 1


def normalize_list(X):
    list = []
    list.append(normalize(0, X[0]))
    list.append(normalize(1, X[1]))
    list.append(normalize(2, X[2]))
    list.append(normalize(3, X[3]))
    return list


def nonlin(x, deriv=False):
    if (deriv == True):
        return (x * (1 - x))
    return 1 / (1 + np.exp(-x))


X = np.array([[1.5, 45, 4, 1.5],  # легковой автомобиль
              [4.5, 99, 45, 2],  # пассажирский автобус
              [8, 150, 3, 6],  # грузовой транспорт
              [0.7, 30, 4, 1],
              [4, 150, 18, 2],
              [1.5, 75, 3, 0.5],
              [6, 250, 4, 5],
              [4, 175, 3, 2],
              [5, 168, 21, 6]])

X_normalized = np.array([normalize_list(X[0]), normalize_list(X[1]), normalize_list(X[2]),
                         normalize_list(X[3]), normalize_list(X[4]), normalize_list(X[5]),
                         normalize_list(X[6]), normalize_list(X[7]), normalize_list(X[8])])

y = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [1, 0, 0],
              [0, 1, 0],
              [1, 0, 0],
              [0, 0, 1],
              [0, 0, 1],
              [0, 1, 0]])

np.random.seed(1)

syn0 = 2 * np.random.random((4, 5)) - 1
syn1 = 2 * np.random.random((5, 3)) - 1

for j in range(100000):
    test = X_normalized
    res = nonlin(np.dot(test, syn0))
    l2 = nonlin(np.dot(res, syn1))

    l2_error = y - l2

    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(res, deriv=True)

    syn1 += res.T.dot(l2_delta)
    syn0 += test.T.dot(l1_delta)

print('обучение на входных данных:')
for el in l2:
    for el2 in el:
        print(int(el2 * 100), '%', sep='', end=' ')
    print(result(el))
print()

print('тестирование на новых вариантах:')
test = np.array([[10, 210, 1, 5],
                 [11, 245, 9, 3],
                 [0.4, 40, 4, 1],
                 [0.3, 15, 3, 0.5],
                 [0.2, 11, 1, 0.6],
                 [5, 205, 22, 8]])
test_normalized = np.array([normalize_list(test[0]), normalize_list(test[1]), normalize_list(test[2]),
                          normalize_list(test[3]), normalize_list(test[4]), normalize_list(test[5])])
res = nonlin(np.dot(nonlin(np.dot(test_normalized, syn0)), syn1))
for el in res:
    for el1 in el:
        print(int(el1 * 100), '%', sep='', end=' ')
    print(result(el))
print()

