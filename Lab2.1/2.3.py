"""
Задание 3.

a) Дано натуральное число. Выведите его последнюю цифру. 

b) Дано положительное действительное число X. Выведите его дробную часть.

c) Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.

d) По российским правилам числа округляются до ближайшего целого числа, а если дробная часть
числа равна 0.5, то число округляется вверх.
"""
import math

print('task a')
print('Input number ')
n = int(input())
print('Result: ', end="")
print(n % 10)

print('task b')
print('Input number ')
x = float(input())
print('Result: ', end="")
if x > 1:
    print(round(x - math.floor(x), 2))
else:
    print(x)

print('task c')
print('Input number ')
x = float(input())
print('Result: ', end="")
print(int(x * 10) % 10)

print('task c')
print('Input number ')
num = float(input())
print('Result: ', end="")
if num - int(num) == 0.5: num += 0.1
print(round(num))
