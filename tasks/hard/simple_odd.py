"""
Написать 2 генератора:
1) Генератор simple_number первый идет по всем простым числам
(число делится только на 1 и на само себя)
2) Генератор odd_simple, который используется значения первого и возвращает
из них нечетные
"""


def simple_number():
    for n in range(10):
        for x in range(2, n):
            if n % x == 0:
                continue
            else:
                yield n


number = simple_number()
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))

# def isprime(n):
#     if n == 1:
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#         else:
#             return True
#
#
# def primes(n=1):
#     while(True):
#         if isprime(n):
#             yield n
#
# print(next(isprime))