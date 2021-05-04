"""
Задание 3.

a) В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом
тексте ранее.

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов
или символами конца строки.

b) Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.

c) Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается
чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

d) Дан текст: в первой строке записано количество строк в тексте, а затем сами строки. Выведите все слова, встречающиеся в
тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию их количества появления в тексте, а при
одинаковой частоте появления — в лексикографическом порядке.

Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости
слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список
кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму. Это почти то, что требуется
в задаче.
"""

print('task a')
print('Input string')
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

print('task b')
print('Input number of elements in dict')
n = int(input())
dict_b = {}
for i in range(n):
    first, second = input().split()
    dict_b[first] = second
    dict_b[second] = first
print('Input needed word: ')
print('Synonym: ', end=' ')
print(dict_b[input()])

print('task c')
print('Input number of words')
n = int(input())
print('Input string')
dict_c = {}

for i in range(n):
    for word in input().split():
        dict_c[word] = dict_c.get(word, 0) + 1

max_count = max(dict_c.values())
most_frequent = [k for k, v in dict_c.items() if v == max_count]
print('Result: ', end=' ')
print(min(most_frequent))
"""
cde abc
efg cde
hij klm
abc cde
abc
"""

print('task d')
print('Input number of words')
n = int(input())
print('Input string')
dict_d = {}
for i in range(n):
    for word in input().split():
        dict_d[word] = dict_d.get(word, 0) + 1

lst = [(k, v) for k, v in dict_d.items()]
lst = sorted(lst)
for el in lst:
    print(el)
