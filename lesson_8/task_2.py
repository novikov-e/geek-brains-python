"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
try:
    if second_number == 0:
        raise MyZeroDivisionError("Деление на ноль невозможно!")
    result = first_number / second_number
except MyZeroDivisionError as err:
    print(err)
else:
    print(f'Результат: {result}')
