"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(some_dict):
    new_dict = {a: b for b, a in some_dict.items()}
    return new_dict


dict1 = {1: 'acc', 2: 'cab', 3: 'ccb'}
print(reverse_dict(dict1))