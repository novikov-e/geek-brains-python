"""
1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
затем выведите на экран.
"""

a = 'Hello'
b = 'World'
c = '!'
print(f'{a} {b} {c}\n')

name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
print(f'Привет {name} {surname}!\n')

print('Сложение двух чисел')
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
result = first_number + second_number
print(f'Сумма = {result}')
