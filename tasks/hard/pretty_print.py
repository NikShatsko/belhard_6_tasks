"""
Написать рекурсивную функцию, которая будет красиво выводить данные в консоль.
Если строчный тип данных, то выводить в кавычках


например:

data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}

{
    'a': 123,
    123: [1, 2, 3],
    'asd': {
        'c': 654.54,
    },
}
"""

from pprint import pprint

data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}

pprint(data)