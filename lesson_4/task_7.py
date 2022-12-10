"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим
очередное значение. При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n). Она отвечает за
получение факториала числа. В цикле нужно выводить только первые n чисел,
начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def factorial(number):
    """
    Функция возвращает факториал числа n
    :param number: число
    :return: факториал
    """
    result = 1
    for element in current_factorial(number):
        result *= element
    return result


def current_factorial(number):
    """
    Функция возвращает генератор с последовательностью натуральных чисел до n
    :param number: число
    :return: генератор
    """
    for element in range(1, number + 1):
        yield element


def print_factorial(number):
    """
    Функция выводит на экран вычисление факториала
    :param number: число
    """
    result = 'Фаториал числа ' + str(number) + ' = '
    for element in current_factorial(number):
        if element == 1:
            result += str(element)
        else:
            result += ' * ' + str(element)
    result += ' = ' + str(factorial(number))
    print(result)


print_factorial(4)
