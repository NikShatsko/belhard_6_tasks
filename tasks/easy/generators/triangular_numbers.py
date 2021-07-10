"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:

Tn = 1 / 2 * n * (n + 1)


Например:

tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers():
    for n in range(1, 10):
        yield 1 / 2 * n * (n + 1)


triangle = triangular_numbers()
print(next(triangle))
print(next(triangle))
print(next(triangle))
print(next(triangle))
print(next(triangle))
print(next(triangle))
print(next(triangle))