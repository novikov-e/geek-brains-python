"""
**7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число». Реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
класса (комплексные числа), выполните сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""
# В Python уже реализован класс Комплексное число
z1 = 3 + 7j
z2 = 2 + 1j
int_complex = 5
float_complex = 2.36
print(type(z1))
print(z1 * z2)
print(z1 + int_complex)
print(z2 * float_complex)
