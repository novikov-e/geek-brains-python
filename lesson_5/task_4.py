"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""

numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("task_4_ru.txt", "w", encoding='utf-8') as output_file:
    with open("task_4_eng.txt", "r", encoding='utf-8') as input_file:
        for line in input_file:
            if line != '':
                input_line = line.split()
                new_line = f'{numerals.get(input_line[0])} ' \
                           f'{input_line[1]} ' \
                           f'{input_line[2]}\n'
                print(new_line)
                output_file.write(new_line)
