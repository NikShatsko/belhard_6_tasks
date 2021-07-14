"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""
SOME_DICT = {str(val): val for val in range(1, 50, 3)}


def muiltiply_dict_values(some_dict):
    result = 1
    for i in some_dict:
        if i == int():
            result = result * some_dict[i]
            return result


print(muiltiply_dict_values(SOME_DICT))