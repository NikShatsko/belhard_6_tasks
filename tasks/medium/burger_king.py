"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""


def bread(func):
    def wrapped():
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrapped


def tomato(func):
    def wrapped():
        print("*** помидоры ****")
        func()
    return wrapped


def salad(func):
    def wrapped():
        print("~~~~ салат ~~~~~")
        func()
    return wrapped


def cheeze(func):
    def wrapped():
        print("^^^^^ сыр ^^^^^^")
        func()
    return wrapped


def onion(func):
    def wrapped():
        print("----- лук ------")
        func()
    return wrapped


def beef(func):
    def wrapped():
        print("### говядина ###")
    return wrapped


def chicken(func):
    def wrapped():
        print("|||| курица ||||")
    return wrapped

@bread
@cheeze
@salad
@chicken
def chikenburger():
    pass


chikenburger()

@bread
@onion
@tomato
@beef
def hamburger():
    pass


hamburger()
