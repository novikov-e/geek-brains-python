"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже
должно быть два элемента — номер товара и словарь с параметрами, то есть
характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например, название. Тогда значение — список
значений-характеристик, например, список названий товаров.

Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

products = list()
analytics = {'Наименование': [], 'Цена': [], 'Кол-во': [], 'Ед. изм.': []}
columns_length = [1, 12, 4, 10, 8]
number = 1
while True:
    print('"Добавить" - Добавить товар')
    print('"Список" - Вывести список товаров')
    print('"Аналитика" - Вывести аналитику')
    print('"Выйти" - Завершить работу программы')
    command = input('Введите команду: ')
    if command == 'Добавить':
        name = input('Наименование: ')
        price = input('Цена: ')
        amount = input('Количество: ')
        unit = input('Единица измерения: ')
        products.append((number, {'Наименование': name,
                                  'Цена': price,
                                  'Кол-во': amount,
                                  'Ед. изм.': unit}))
        number += 1
        analytics['Наименование'].append(name)
        analytics['Цена'].append(price)
        analytics['Кол-во'].append(amount)
        analytics['Ед. изм.'].append(unit)
    elif command == 'Список':
        for product in products:
            number = str(tuple(product).__getitem__(0))
            if len(number) > columns_length[0]:
                columns_length[0] = len(number)
            data = tuple(product).__getitem__(1)
            if len(data.get('Наименование')) > columns_length[1]:
                columns_length[1] = len(data.get('Наименование'))
            if len(data.get('Цена')) > columns_length[2]:
                columns_length[2] = len(data.get('Цена'))
            if len(data.get('Кол-во')) > columns_length[3]:
                columns_length[3] = len(data.get('Кол-во'))
            if len(data.get('Ед. изм.')) > columns_length[4]:
                columns_length[4] = len(data.get('Ед. изм.'))
        print(f'|{"№":^{columns_length[0]}}'
              f'|{"Наименование":^{columns_length[1]}}'
              f'|{"Цена":^{columns_length[2]}}'
              f'|{"Кол-во":^{columns_length[3]}}'
              f'|{"Ед. изм.":^{columns_length[4]}}|')
        line_length = columns_length[0] + columns_length[1] + columns_length[2] + \
                      columns_length[3] + columns_length[4] + 6
        print('-' * line_length)
        for product in products:
            number = str(tuple(product).__getitem__(0))
            data = tuple(product).__getitem__(1)
            print(f'|{number:^{columns_length[0]}}'
                  f'|{data.get("Наименование"):<{columns_length[1]}}'
                  f'|{data.get("Цена"):^{columns_length[2]}}'
                  f'|{data.get("Кол-во"):^{columns_length[3]}}'
                  f'|{data.get("Ед. изм."):^{columns_length[4]}}|')
    elif command == 'Аналитика':
        for item in analytics.items():
            print(item)
    elif command == 'Выйти':
        break
    else:
        print('Не правильно введена команда!')
