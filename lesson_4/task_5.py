"""
5. Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти чётные числа от 100 до 1000
(включая границы). Нужно получить результат вычисления произведения всех
элементов списка.

Подсказка: использовать функцию reduce().
"""
from functools import reduce

my_list = (el for el in range(100, 1001) if el % 2 == 0)


def multiply(first, second):
    """
    Функция вычисляет произведение двух чисел
    :param first: первое число
    :param second: второе число
    :return: произведение
    """
    return first * second


print(reduce(multiply, my_list))
