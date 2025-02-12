"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def sum_of_digit(n: int):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(n // 10)


print(sum_of_digit(25))