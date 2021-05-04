"""
Задание 1.

a) Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние
между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.

b) Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень можно пользоваться для проверки результата.

c) Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую
букву на большую.

Например, print(capitalize('word')) должно печатать слово Word.

На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв.
Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте вашу
функцию capitalize().

Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII, и функция chr(),
которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.

d) Напишем функцию max(), которая принимает переменное число аргументов и возвращает максимум из них (на самом деле
такая функция уже встроена в Питон).

e) В написанную в пункте a) программу добавьте обработку не менее двух типов исключений.
"""

import math

print('task a')


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print('Input 4 numbers: ')
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print('Result: ', distance(x1, y1, x2, y2))

print('task b')


def power(a, n):
    if n == 0:
        return 1
    else:
        res = a
        for i in range(n - 1):
            res *= a
            i += 1

        return res


# n == 1 ? a : a * power(a,n-1)

print('Input a and n: ')
a = float(input())
n = int(input())
print('Result: ', power(a, n))

print('task c')


def capitalize(str):
    return str.title()


print('Input words: ')
for word in input().split():
    print(capitalize(word), end=' ')


print()
print('task d')


def max(*args):
    max = args[0]
    for i in args:
        if i > max:
            max = i
    return max


a = 15
b = 13
c = 2
d = 5
e = 10

print('Result for 2 args: ', max(a, b))
print('Result for 3 args: ', max(c, d, e))
print('Result for 4 args: ', max(d, b, c, e))

print('task e')
print('Input 4 numbers: ')
try:
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print('Это что ещё такое?')
else:
    print('Result: ', distance(x1, y1, x2, y2))
