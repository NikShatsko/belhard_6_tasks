"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(some_list):
    if some_list == list:
        return some_list
    if isinstance(some_list[0], list):
        return some_list


list1 = [1, 2, [1, 2, [5, 7], 3], 8]

print("\t" * line_print(list1))

