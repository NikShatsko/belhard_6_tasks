"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(n: dict):
    school_data['1a'] += 1
    school_data['1b'] += 1
    school_data['2a'] += 1
    school_data['2b'] += 1
    return school_data


def decr_students(n: dict):
    school_data['1a'] -= 1
    school_data['1b'] -= 1
    school_data['2a'] -= 1
    school_data['2b'] -= 1
    return school_data


def add_class(n: dict):
    school_data['3a'] = 0
    return school_data


def remove_class(n: dict):
    del school_data['2a']
    return school_data


def calc_students(n: dict):
    return sum(school_data.values())


print(incr_students(school_data))
print(decr_students(school_data))
print(add_class(school_data))
print(remove_class(school_data))
print(calc_students(school_data))