"""
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и
возвращает словарь, в котором каждый элемент списка является и ключом и
значением. Предполагается, что элементы списка будут соответствовать
правилам задания ключей в словарях.
"""


# def to_dict(lst):
#     return {element: element for element in lst}
#
#
# print(to_dict([1, 'a', 'hello', 4]))

def to_dict(lst):
    some_dict = {}
    for i in lst:
        some_dict[i] = i
    return some_dict


print(to_dict([1, 'a', 'hello', 4]))