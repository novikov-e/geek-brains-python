"""
7. Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10%
относительно предыдущего. Требуется определить номер дня, на который
результат спортсмена составит не менее b километров. Программа должна
принимать значения параметров a и b и выводить одно натуральное число — номер
дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""

a = float(input('Текущая дистанция: '))
b = float(input('Итоговая дистаниция: '))
day = 1
while a < b:
    a += a * 0.1
    day += 1
print(f'Необходимо {day} дней')
