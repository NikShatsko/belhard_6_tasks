"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и 
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def is_power(n):
    n = n/2
    if n == 1:
        return True
    if n == 2:
        return True
    elif n > 2:
        return is_power(n)
    else:
        return False


print(is_power(64))