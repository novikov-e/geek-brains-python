"""
3. Реализовать базовый класс Worker (работник).
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
- создать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров.
"""


class Worker:
    """
    Класс описывает сотрудника
    """
    def __init__(self, name, surname, position, wage, bonus):
        """
        Конструктор
        :param name: Имя
        :param surname: Фамилия
        :param position: Должность
        :param wage: Оклад
        :param bonus: Премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position (Worker):
    """
    Класс описывает должность
    """
    def get_full_name(self):
        """
        Возвращает полное имя сотрудника
        :return: Имя и фамилия
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
        Возвращает полный доход
        :return: доход
        """
        return self._income['wage'] + self._income['bonus']


developer = Position('Egor', 'Novikov', 'Программист', 60000, 15000)
print(developer.get_full_name())
print(developer.get_total_income())
