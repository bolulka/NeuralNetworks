"""
Задание 2.  (из  темы  4.1, нейросеть в три слоя):

* увеличьте число нейронов во втором слое,
* увеличите число слоев, проанализируйте результаты,
* обучите нейронную сеть для <исключающего или>, рассмотренную в теме 1,
* увеличьте число слоев для этой нейронной сети, проанализируйте результаты,
* реализуйте 11 строк кода с первой страницы, сравните результаты.

"""
import numpy as np


def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))


X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((3, 5)) - 1
syn1 = 2 * np.random.random((5, 3)) - 1
syn2 = 2 * np.random.random((3, 1)) - 1

for j in range(60000):

    # проходим вперёд по слоям 0, 1 и 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))

    # как сильно мы ошиблись относительно нужной величины?
    l3_error = y - l3
    if (j % 10000) == 0:
        print
        "Error:" + str(np.mean(np.abs(l3_error)))

    l3_delta = l3_error * nonlin(l3, deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print('First: ')
print(l3)

X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

y = np.array([[0, 1, 1, 0]]).T

syn0 = 2 * np.random.random((3, 4)) - 1

syn1 = 2 * np.random.random((4, 1)) - 1

for j in range(60000):
    l1 = 1 / (1 + np.exp(-(np.dot(X, syn0))))

    l2 = 1 / (1 + np.exp(-(np.dot(l1, syn1))))

    l2_delta = (y - l2) * (l2 * (1 - l2))

    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))

    syn1 += l1.T.dot(l2_delta)

    syn0 += X.T.dot(l1_delta)

print('Second: ')
print(l2)
