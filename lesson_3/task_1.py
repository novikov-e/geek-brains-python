"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""


def division(first_num, second_num):
    """
    Функция производит деление числа а на число b
    :param first_num: частное
    :param second_num: делитель
    :return: результат
    """
    try:
        return first_num / second_num
    except ZeroDivisionError:
        print('Деление на ноль недопустимо!')
    return None


try:
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))
    print(division(first_number, second_number))
except ValueError:
    print('Пожалуйста введите число!')
