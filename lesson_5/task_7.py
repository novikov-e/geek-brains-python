"""
7. **Создать вручную и заполнить несколькими строками текстовый файл, в котором
каждая строка будет содержать данные о фирме: название, форма собственности,
выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не
включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

with open("task_7.txt", "r", encoding='utf-8') as input_file:
    firms_dict = {}
    average_profit_dict = {}
    all_profit = 0
    count = 0
    for line in input_file:
        if line != '':
            split_line = line.split()
            name = split_line[0]
            profit = float(split_line[2]) - float(split_line[3])
            firms_dict[name] = profit
            if profit > 0:
                all_profit += profit
                count += 1
    average_profit_dict['average_profit'] = all_profit / count
    with open('task_7.json', 'w', encoding='utf8') as json_file:
        json.dump([firms_dict, average_profit_dict], json_file)