"""
1. Создать класс TrafficLight (светофор).
- Определить у него один атрибут color
- (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный,
 жёлтый, зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
import sys
import time


class TrafficLightColor:
    """
    Класс описывает конфигурацию режима светофора
    """
    def __init__(self, name, seconds, color):
        self.name = name
        self.seconds = seconds
        self.color = color


class TrafficLight:
    """
    Класс описывает работу светофора
    """
    __color = None
    config = [TrafficLightColor('RED', 7, 31),
              TrafficLightColor('YELLOW', 2, 33),
              TrafficLightColor('GREEN', 10, 32),
              TrafficLightColor('YELLOW', 2, 33)]

    def run(self):
        """
        Метод запускает светофор
        """
        while True:
            for color in self.config:
                sys.stdout.write('\r')
                sys.stdout.flush()
                sys.stdout.write("\033[{}m{}".format(color.color, color.name))
                sys.stdout.flush()
                time.sleep(color.seconds)
                self.__color = color


traffic_light = TrafficLight()
traffic_light.run()
