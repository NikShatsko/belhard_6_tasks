"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(n):
    a, b = 1, 1
    if n < 1:
        raise ValueError(f"Введите значение больше 1")
    for i in range(n):
        yield a
        a, b = b, a + b



fibonacci_gen = fibonacci(0)
print(fibonacci_gen)
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))