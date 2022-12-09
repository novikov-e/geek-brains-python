"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с
каким финансовым результатом работает фирма. Например, прибыль — выручка
больше издержек, или убыток — издержки больше выручки. Выведите
соответствующее сообщение.

6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это
отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчёте на одного сотрудника.
"""
revenue = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))
result = round(revenue - costs, 2)
if revenue > costs:
    print(f'Выручка превысила издержки на {"%#.2F" % (result)} руб.')
    profitability = result / revenue * 100
    print(f'Рентабельность составила: {"%d" % (profitability)}%')
    amount_of_emloyees = int(input('Введите численность сотрудников: '))
    profit_per_person = result / amount_of_emloyees
    print(f'Прибыль в расчёте на одного человека сотавляет: '
          f'{"%#.2F" % (profit_per_person)} руб.')
elif costs > revenue:
    print(f'Издержки превысили выручку на {"%#.2F" % (abs(result))} руб.')
else:
    print('Выручка равна издержкам')