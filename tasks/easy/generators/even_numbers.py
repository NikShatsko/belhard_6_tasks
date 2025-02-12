"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    for n in range(10):
        if n > 0:
            if n % 2 == 0:
                yield n


number = get_even_number()
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))