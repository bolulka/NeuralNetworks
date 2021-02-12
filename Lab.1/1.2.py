import numpy as np


def sigmoid(x):
    # Функция активации sigmoid:: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # Производная от sigmoid: f'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)

def get_final_W(network):
    w_final = [network.w1, network.w2, network.w3, network.w4, network.w5, network.w6]
    return w_final

def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


w = [0.45, 0.78, -0.12, 0.13, 1.5, -2.3]


class NeuralNetwork:

    def __init__(self):
        # Вес
        self.w1 = w[0]
        self.w2 = w[1]
        self.w3 = w[2]
        self.w4 = w[3]
        self.w5 = w[4]
        self.w6 = w[5]

    def feedforward(self, x):
        # x является массивом numpy с двумя элементами
        h1 = sigmoid(self.w1 * x[0] + self.w3 * x[1])
        h2 = sigmoid(self.w2 * x[0] + self.w4 * x[1])
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2)
        return o1

    def train(self, data, true_res):
        learn_rate = 0.1
        epochs = 1000  # количество циклов во всём наборе данных

        for epoch in range(epochs):
            for x, y_true in zip(data, true_res):
                # --- Обратная связь
                sum_h1 = self.w1 * x[0] + self.w3 * x[1]
                h1 = sigmoid(sum_h1)

                sum_h2 = self.w2 * x[0] + self.w4 * x[1]
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2
                o1 = sigmoid(sum_o1)
                y_pred = o1

                # --- Подсчет частных производных
                # --- Наименование: d_L_d_w1 представляет "частично L / частично w1"
                d_L_d_ypred = -2 * (y_true - y_pred)

                # Нейрон o1
                d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)

                # Нейрон h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w3 = x[1] * deriv_sigmoid(sum_h1)

                # Нейрон h2
                d_h2_d_w2 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)

                # --- Обновляем вес и смещения
                # Нейрон h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w3

                # Нейрон h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w2
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4

                # Нейрон o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6


# Тренировочный сет
data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
true_res = [0, 1, 1, 0]

network = NeuralNetwork()
network.train(data, true_res)
print('Result on different sets: ')
x_res = np.apply_along_axis(network.feedforward, 1, data)
print(x_res)

err = mse_loss(true_res, x_res)
print('Total error:')
print(err)

print('Best vector W:')
print(get_final_W(network))
