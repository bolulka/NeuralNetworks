import numpy as np


def sigmoid(x):
    #  f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


X = [1, 0]
W = [0.45, 0.78, -0.12, 0.13, 1.5, -2.3]


class NeuralNetwork:

    def __init__(self):
        # Вес
        self.w1 = W[0]
        self.w2 = W[1]
        self.w3 = W[2]
        self.w4 = W[3]
        self.w5 = W[4]
        self.w6 = W[5]

    def feedforward(self, X):
        # x является массивом numpy с двумя элементами
        h1 = sigmoid(self.w1 * X[0] + self.w3 * X[1])
        h2 = sigmoid(self.w2 * X[0] + self.w4 * X[1])
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2)
        return o1


network = NeuralNetwork()
print('Result: ')
print(network.feedforward(X))

print('Error: ')
print(mse_loss(1, network.feedforward(X)))

