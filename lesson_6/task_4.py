"""
4. Реализуйте базовый класс Car.
- у класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    speed = 0
    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} начал движение')

    def turn(self, direction):
        print(f'{self.name} повернул на {direction}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановился')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('Внимание превышение скорости!')


class SportCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_police = False


class WorkCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_police = True

    def show_speed(self):
        if self.speed > 40:
            print('Внимание превышение скорости!')


class PoliceCar(Car):
    def __init__(self, name):
        self.name = name
        self.color = 'WHITE'
        self.is_police = True


car = Car('Volkswagen', 'BLUE', False)
car.go(60)
car.speed = 30
car.turn('право')
car.speed = 60
car.speed = 30
car.turn('лево')
car.speed = 50
car.show_speed()
car.stop()

work_car = WorkCar('Ford', 'GREEN')
work_car.go(60)
work_car.show_speed()
work_car.stop()

town_car = TownCar('Toyota', 'RED')
town_car.go(70)
town_car.show_speed()
town_car.stop()
