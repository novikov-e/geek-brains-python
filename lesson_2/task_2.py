"""
2. Для списка реализовать обмен значений соседних элементов. Значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве
элементов последний сохранить на своём месте. Для заполнения списка элементов
нужно использовать функцию input().
"""

input_list = input('Введите значения списка разделяя их пробелом: ').split()
i = 2
while i <= len(input_list):
    value = input_list[i - 1]
    input_list[i - 1] = input_list[i - 2]
    input_list[i - 2] = value
    i += 2
print(input_list)
