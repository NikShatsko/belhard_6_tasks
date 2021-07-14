"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(a1, a2, a3, symmetric=False):
    if symmetric is False:
        return a1 - a2 - a3
    else:
        return a1.symmetric_difference(a2), a1.symmetric_difference(a3), a2.symmetric_difference(a3)


a1 = {2, 3, 5}
a2 = {2, 7, 6}
a3 = {1, 5, 1}

print(set_diff(a1, a2, a3))
