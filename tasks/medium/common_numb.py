"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""


def common_numbers(list1: list, list2: list):
    list3 = []
    for i in list1:
        for j in list2:
            if j == i:
                list3.append(j)
    return sorted(list3, reverse=True)


print(common_numbers([1, 2, 3, 5, 6], [1, 4, 3, 6, 8]))