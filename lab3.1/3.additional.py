"""
ДОП.  В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.

Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0,
у любого другого элемента высота на 1 больше, чем у его родителя.

Вам дано генеалогическое древо, определите высоту всех его элементов.

Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для
каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента
необходимо вывести его высоту.

Примечание

Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2) (не считая сложности обращения
к элементам словаря).
"""


def height(person):
    if person not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[person])


p_tree = {}
print('Input N:')
n = int(input())
print('Input child and parent: ')
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
for person in set(p_tree.keys()).union(set(p_tree.values())):
    heights[person] = height(person)

for key, value in sorted(heights.items()):
    print(key, value)

"""
n=5

Masha Dasha
Kattie Mickle
Mickle Robbie
Teodor Robbie

Result:

Dasha 0
Kattie 2
Masha 1
Mickle 1
Robbie 0
Teodor 1
"""