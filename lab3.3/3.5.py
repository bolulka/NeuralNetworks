"""
Задание 2

a) Вычислите логарифм по основанию 2 от 15.

b) Сгенерируйте четыре раза одно и то же число, равномерно распределенное на интервале (0; 1).

c) Определите список имен, определенных в данный момент.

d) Создайте и выполните свой модуль на языке Python.
"""
import math
import numpy as np
import module_task_d


print('task a')
print('Result: log2(15)= ', math.log2(15))

print('task b')
np.random.seed(1)
print('First number', np.random.uniform(0, 1))
np.random.seed(1)
print('Second number', np.random.uniform(0, 1))
np.random.seed(1)
print('Third number', np.random.uniform(0, 1))
np.random.seed(1)
print('Fourth number', np.random.uniform(0, 1))

print('task c')
print(str(dir()))

app = module_task_d.Dialog()
app.mainloop()
