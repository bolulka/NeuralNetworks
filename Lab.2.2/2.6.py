"""
Задание 6

a) Определите: сколько гласных и сколько согласных букв в строке.

b) Дано предложение, слова которого отделены пробелами, в конце предложения точка.
Напишите каждое слово, начиная его с большой буквы и заканчивая точкой.

c) Дана строка. Определите частоту, с которой входят разные буквы в эту строку.

d) Дана строка. Группы символов между пробелами считаются словами. Определите
сколько слов начинается и заканчивается одной и той же буквой.

e) Создайте список из случайных целочисленных значений. Определите максимальный
и минимальный элементы в нем. Если таких элементов несколько, то выведите значение и
индексы всех таких элементов.

f) В списке перепишите все ненулевые элементы в начало списка (сохраняя порядок),
а нулевые - в конец.

g) Получите список из положительных элементов другого списка, стоящих на четных местах.

h) В списке чисел найти самую длинную последовательность, которая упорядочена по
возрастанию. Если таких последовательностей несколько (с одинаковой максимальной длинной), то найти их все.
Вывести на экран сам список, длину самой длинной упорядоченной по возрастанию последовательности,
саму последовательность (или несколько).
"""
import random

print('task a')
print('Input string ')
str = input()
print('Result: ', end="")
vowels = 0
consonants = 0
cyrillic_vowels = ['а', 'е', 'и', 'у', 'ы', 'э', 'ю', 'я']
latin_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for i in str:
    letter = i.lower()
    if letter in cyrillic_vowels or letter in latin_vowels:
        vowels += 1
    else:
        consonants += 1
print('vowels: ', vowels, ', consonants: ', consonants)


print('task b')
print('Input sentence ')
s = input().split()
print('Result: ', end="")
for i in s:
    print(i.title(), end=". ")
print()

print('task c')
print('Input sentence ')
a = input().lower()
all_freq = {}
print('Result: ', end="")
for i in a:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(str(all_freq))

print('task d')
print('Input sentence ')
st = input().split()
counter = 0
print('Result: ', end="")
for i in st:
    if i[0] == i[-1]:
        counter += 1
print(counter)

print('task e')
sample = [1, 1, 2, 5, 2, 3, 4, 5, 8, 20, 19, 20, 15, 4]
list = random.sample(sample, 10)
print('List: ', list)
list.sort()
print('Result: ', end="")
counter_min = list.count(list[0])
counter_max = list.count(list[len(list) - 1])
indexes_min = range(0, counter_min - 1)
indexes_max = range(len(list) - counter_min - 1, len(list) - 1)
if counter_max > 1 and counter_min > 1:
    print('min: ', list[0], ', indexes: ', indexes_min, ', max: ', list[len(list) - 1], ', indexes: ', indexes_max)
elif counter_max > 1 and counter_min == 1:
    print('min: ', list[0], ', max: ', list[len(list) - 1], ', indexes: ',
          indexes_max)
elif counter_max == 1 and counter_min > 1:
    print('min: ', list[0], ', indexes: ', indexes_min, ', max: ', list[len(list) - 1])
else:
    print('min: ', list[0], ', max: ', list[len(list) - 1])

print('task f')
print('Input list ')
lst = [int(i) for i in input().split()]
print('Result: ', end="")
zero_list = [str(i) for i in lst if not (int(i))]
print(' '.join(str(i) for i in lst if int(i)), ' '.join(zero_list))

print('task g')
print('Input list ')
list_g = [int(i) for i in input().split()]
print('Result: ', end="")
new_list = list(ind for ind, item in enumerate(list_g) if ind % 2 == 0 and list_g[ind] >= 0)
print(new_list)
# 0 1 -2 3 4 5 -6 7 8
# Result: [0, 4, 8]

print('task h')
list_h = random.sample(range(1, 20), 15)
print('List: ', list_h)
cur_len = 1
max_len = 1
print('Result: ')
for i in range(1, len(list_h)):
    if list_h[i] > list_h[i - 1]:
        cur_len += 1
    else:
        if cur_len > max_len:
            max_len = cur_len
        cur_len = 1
cur_len = 1
for i in range(1, len(list_h)):
    if list_h[i] > list_h[i - 1]:
        cur_len += 1
        if i == len(list_h) - 1 and cur_len == max_len: print('Max len: ', max_len, ', sequence: ',
                                                              list(list_h[ind] for ind in range(i - max_len + 1, i + 1)))
    else:
        if cur_len == max_len:
            print('Max len: ', max_len, ', sequence: ', list(list_h[ind] for ind in range(i - max_len, i)))
        cur_len = 1
# test1 = [2, 15, 6, 17, 11, 7, 12, 19, 13, 9, 3, 10, 18, 8, 14]
# test2 =[17, 7, 9, 4, 2, 8, 5, 13, 6, 15, 16, 19, 10, 12, 11]
# test3 = [15, 7, 4, 12, 9, 11, 16, 6, 14, 10, 1, 13, 2, 8, 19]
# test4 = [9, 15, 3, 2, 18, 17, 11, 7, 6, 5, 4, 1, 10, 13, 12]
# test5 = [1, 16, 10, 6, 17, 5, 7, 3, 11, 18, 2, 12, 13, 9, 4]