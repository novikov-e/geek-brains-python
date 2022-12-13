"""
3. Создать текстовый файл (не программно). Построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.

Пример файла:

Иванов 23543.12
Петров 13749.32
"""
from functools import reduce

with open("task_3.txt", "r", encoding='utf-8') as input_file:
    employees = {}
    for line in input_file:
        if line != '':
            employee = line.split()
            employees[employee[0]] = float(employee[1])
    average_wage = reduce(
        lambda first, second: first + second,
        employees.values()) / len(employees.values())
    print(f'Средняя величина дохода сотрудников: {average_wage:.2f} руб.')
    print('Сотрудники с окладом ниже 20000.00 руб.')
    for employee, wage in employees.items():
        if wage < 20000.0:
            print(employee)
