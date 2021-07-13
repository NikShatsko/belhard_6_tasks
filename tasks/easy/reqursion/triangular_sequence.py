"""
Написать функцию triangular_sequence, которая принимает n и выводит
следующую последовательность

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, current=1):
    if current <= n:
        print(str(current) * current)
        triangular_sequence(n, current + 1)


triangular_sequence(6)