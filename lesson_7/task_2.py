"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для
костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для
пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на
реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod
from functools import reduce


# rate - расход
class Dress(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def rate(self):
        pass


class Coat(Dress):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def rate(self):
        return self.size / 6.5 + 0.5


class Costume(Dress):
    def __init__(self, name, growth):
        super().__init__(name)
        self.growth = growth

    def rate(self):
        return self.growth * 2 + 0.3


order = {Coat('Первая модель пальто', 2.3): 6,
         Coat('Вторая модель пальто', 1.7): 12,
         Costume('Первая модель костюма', 3): 5,
         Costume('Вторая модель костюма', 2.4): 14}


amount_of_fabric = reduce(lambda first, second: first + second,
                          (k.rate() * v for k, v in order.items()))
print(f'Общее количество ткани: {amount_of_fabric:.2f} кв.м')