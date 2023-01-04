"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime
import re


def validate_date_format(date):
    if type(date) is str and re \
            .compile(r"^[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]$") \
            .search(date):
        return True
    else:
        raise TypeError('Некорректно введена дата! '
                        'Введите дату строкой в формате дд-мм-гггг!')


class CorrectDate:
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if MyDate.validate(value):
            instance.__dict__[self.my_attr] = value


class MyDate:
    date = CorrectDate('date')

    def __init__(self, date):
        try:
            self.date = date
        except TypeError as error:
            print(error)

    @classmethod
    def to_number(cls, date):
        try:
            if validate_date_format(date):
                return [int(x) for x in date.split('-')]
        except TypeError as error:
            print(error)

    @staticmethod
    def validate(date):
        try:
            if validate_date_format(date):
                parse_date = MyDate.to_number(date)
                datetime.date(parse_date[2], parse_date[1], parse_date[0])
                return True
        except TypeError as error:
            print(error)
            return False
        except ValueError as error:
            print(error)
            return False


# Невисокосный год 29 февраля
print(MyDate.validate('29-02-2003'))
# День и месяц поменяли местами
print(MyDate.validate('02-15-2004'))

try:
    first_date = MyDate('15 февраля 2022')
    print(first_date.date.__dict__['date'])
except KeyError as error:
    print(f'Нет элемента с ключом: {error}')
