"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

with open("task_1.txt", "r", encoding='utf-8') as input_file:
    i = 1
    for line in input_file:
        print(f'Строка {i}. Кол-во слов: {len(line.split())}')
        i += 1
