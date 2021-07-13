"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n):
    def closure(x):
        return x * n
    return closure


first = multiply(5)
print(first(2))