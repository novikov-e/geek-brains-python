"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""
from typing import List


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for line in self.matrix:
            for item in line:
                result += f'{str(item)} '
            result += '\n'
        return result

    def __add__(self, other):
        check = True
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    check = False
        else:
            check = False
        if check:
            result = []
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[i])):
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Matrix(result)
        else:
            print('Вы пытаетесь сложить матрицы разных размеров!')


first_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
second_matrix = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
third_matrix = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
print(first_matrix + second_matrix)
print(second_matrix + third_matrix)
