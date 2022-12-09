"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""


def sum_of_large(a, b, c):
    """
    Функция возвращает сумму двух наибольших аргументов
    :param a: аргумент
    :param b: аргумент
    :param c: аргумент
    :return: сумма двух наибольших аргументов
    """
    if a >= b:
        if b >= c:
            return a * b
        else:
            return a * c
    else:
        if a >= c:
            return b * a
        else:
            return b * c


print(sum_of_large(2, 4, 6))
print(sum_of_large(2, 6, 4))
print(sum_of_large(6, 2, 4))
print(sum_of_large(6, 4, 2))
print(sum_of_large(4, 2, 6))
print(sum_of_large(4, 6, 2))
