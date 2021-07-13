"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""


def factorial(n: int, result: int = 1):
    if n > 0:
        return factorial(n - 1, result * n)
    else:
        return result


print(factorial(4))