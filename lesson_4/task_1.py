"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника. Используйте в нём формулу: (выработка в
часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, wage, hour_of_work, bonus = argv
result = int(wage) * int(hour_of_work) + int(bonus)
print(f'Итого: {result}')
