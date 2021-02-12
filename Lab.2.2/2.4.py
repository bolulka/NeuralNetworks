"""
Задание 4

a) Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
Используйте для решения задачи метод count.

b) Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами.
Результат запишите в строку и выведите получившуюся строку.

При решении этой задачи не стоит пользоваться циклами и инструкцией if.

c) Дана строка. Замените в этой строке все цифры 1 на слово one.

d) Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое и
последнее вхождение буквы h, а также все символы, находящиеся между ними.
"""

print('task a')
print('Input string ')
print('Result: ', end="")
print(input().count(' ') + 1)

print('task b')
print('Input 2 words separated by space ')
s = input()
print('Result: ', end="")
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(second_word + ' ' + first_word)

print('task c')
print('Input string with few "1" ')
print('Result: ', end="")
print(input().replace('1', 'one'))

print('task d')
print('Input string with few "h" (>2) ')
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print('Result: ', end="")
print(s)

