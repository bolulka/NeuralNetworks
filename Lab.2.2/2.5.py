"""
Задание 5

a) Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

b) Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

c) Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух
своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не
учитываются, поскольку у них недостаточно соседей.

d) В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

e) Дан список-массив, заполненный случайным образом нулями и единицами (сформируйте его). Найдите
самую длинную непрерывную последовательность единиц и определите индексы первого и последнего элементов в ней.
"""

print('task a')
print('Input list ')
list = input().split()
print('Result: ', end="")
for i in range(0, len(list), 2):
    print(list[i], end=" ")
print()

print('task b')
print('Input list ')
str = [int(i) for i in input().split()]
print('Result: ', end="")
for i in range(1, len(str)):
    if str[i] > str[i - 1]:
        print(str[i], end=" ")
print()

print('task c')
print('Input list ')
a = [int(i) for i in input().split()]
counter = 0
print('Result: ', end="")
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)

print('task d')
print('Input list ')
a = [int(s) for s in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print('Result: ', end="")
print(a)

print('task d')
print('List: ', end="")
data = [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
print(data)
start = 0
end = 0
cur_len = 0
max_len = 0
for i in range(len(data)):
    if data[i] == 1:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            start = i - cur_len + 1
    else:
        cur_len = 0
end = start + max_len
print('Len: {}, start: {}, end: {}'.format(max_len, start, end))
