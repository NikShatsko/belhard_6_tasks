"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list):
    new_list = []
    for i in some_list:
        if i in new_list:
            print('Yes')
        else:
            new_list.append(i)
            print('No')


new_list1 = [1, 2, 3, 5, 1]
yes_or_no(new_list1)