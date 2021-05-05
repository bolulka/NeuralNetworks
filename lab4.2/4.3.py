"""
Задание 1.  (из  темы  4.2, тест 1):

Построить прогноз курса доллара США на основе курсов за 4 предшествующих дня на основе имеющихся у нас значений
курса за 13 дней начиная с 01.01.2019: https://www.nbrb.by/statistics/Rates/RatesDaily.asp.
"""
import numpy as np


# Сигмоида
def nonlin(x, deriv=False):
    if (deriv == True):
        return (x * (1 - x))

    return 1 / (1 + np.exp(-x))


# набор входных данных нормализованные
X = np.array([[0.5971, 0.6034, 0.6155],
              [0.6034, 0.6155, 0.6272],
              [0.6155, 0.6272, 0.6279],
              [0.6272, 0.6279, 0.6262]])

# выходные данные
y = np.array([[0.6272, 0.6279, 0.6262, 0.6262]]).T  # 25,26,27,28

# сделаем случайные числа более определёнными
np.random.seed(1)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((3, 5)) - 1
syn1 = 2 * np.random.random((5, 3)) - 1
syn2 = 2 * np.random.random((3, 1)) - 1

for j in range(35000):
    # проходим вперёд по слоям 0, 1 и 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))

    # как сильно мы ошиблись относительно нужной величины?
    l3_error = y - l3
    l3_delta = l3_error * nonlin(l3, deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

example = [0.6279, 0.6262, 0.6262]
l = nonlin(np.dot(example, syn0))
print('29 число: ', 2 + l[0])
