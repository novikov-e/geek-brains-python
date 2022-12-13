"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить её на экран.
"""

with open("task_5.txt", "w", encoding='utf-8') as output_file:
    output_file.writelines((str(f'{i} ') for i in range(1, 26)))

with open("task_5.txt", "r", encoding='utf-8') as input_file:
    result = 0
    for line in input_file:
        for number in line.split():
            result += int(number)
    print(result)
