"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(some_str):
    counter = {}
    for i in some_str:
        n = counter.setdefault(i, 0)
        counter[i] = n + 1
    return counter
    res = list(zip(some_str, counter))
    return res


print(dict_from_str(STR_VAL))
