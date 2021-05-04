"""
Задание 2.

a) Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

Примечание. Эту задачу на Питоне можно решить в одну строчку.

b) Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной
строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

c) Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны
по цвету. Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк, поэтому вам предлагается помочь
им в оставшейся части.

В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. В следующих N строках заданы номера цветов
кубиков Ани. В последних M строках номера цветов Бори.

Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков, которые есть только у Ани
и номера цветов кубиков, которые есть только у Бори. Для каждого из множеств выведите сначала количество элементов в нем, а
затем сами элементы, отсортированные по возрастанию.

d) Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для
этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть
задуманное или NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала
и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

В первой строке задано n - максимальное число, которое мог загадать Август. Далее каждая строка содержит вопрос Беатрисы
(множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.

Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
"""

# print('task a')
# list1 = [1, 1, 2, 5, 3, 4, 8, 9, 6, 6]
# list2 = [1, 3, 5, 4, 10, 9, 12, 13]
# print('List 1: ', list1)
# print('List 2: ', list2)
# counter = len(set(list1) & set(list2))
# print('Number of common elements: ', counter)
# print()
#
# print('task b')
# print('Input numbers,separated by space: ')
# numbers = [int(s) for s in input().split()]
# occur_before = set()
# for num in numbers:
#     if num in occur_before:
#         print('YES')
#     else:
#         print('NO')
#         occur_before.add(num)
# print()

# print('task c')
# print('Input N and M:')
# N, M = [int(s) for s in input().split()]
# A_colors, B_colors = set(), set()
# print('Input N numbers: ')
# for i in range(N):
#     A_colors.add(int(input()))
# print('Input M numbers: ')
# for i in range(M):
#     B_colors.add(int(input()))
#
# print('Result: ')
# print('Common colors[ size:', len(A_colors & B_colors), ', numbers: ',
#       *[str(item) for item in sorted(A_colors & B_colors)], ']')
# print('Ann s colors[ size:', len(A_colors - B_colors), ', numbers: ',
#       *[str(item) for item in sorted(A_colors - B_colors)], ']')
# print('Borya colors[ size:', len(B_colors - A_colors), ', numbers: ',
#       *[str(item) for item in sorted(B_colors - A_colors)], ']')

print('task d')
print('Input n: ')
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
print('Input guesses: ')
while True:
    inp = input()
    if inp == 'STOP' or len(possible_nums) == 1:
        break
    answer = ''.join(filter(str.isalpha, inp)) or None
    guess_ = inp[0:-len(answer)].split()
    guess = set([int(item) for item in guess_])
    if answer == 'YES':
        possible_nums &= guess
        if len(possible_nums) == 1: break
    else:
        possible_nums &= all_nums - guess
        if len(possible_nums) == 1: break

print('Result: ',end=' ')
print(possible_nums)
