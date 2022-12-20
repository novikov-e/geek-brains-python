"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для
классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
ксерокс). В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа
оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру (например,
словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум
возможностей, изученных на уроках по ООП.
"""


class NegativeNumber(Exception):
    """
    Исключение возникает при вводе числа не являющегося положительным.
    """
    def __init__(self, txt):
        self.txt = txt


def validate_number(number):
    """
    Функция проверяет положительное ли число, и в случае если это не так,
    вызывает исключение NegativeNumber.
    :param number: Число.
    :return: Число.
    """
    if int(number) < 0:
        raise NegativeNumber('Значение не может быть отрицательным!')
    else:
        return number


class NotNegativeInt:
    """
    Дескриптор проверяющий что число положительное.
    """
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        instance.__dict__[self.my_attr] = validate_number(value)


class WarehouseItem:
    """
    Ячейка склада
    """
    count = NotNegativeInt('count')

    def __init__(self, office_equipment, count, subdivision):
        """
        Конструктор.
        :param office_equipment: Офисная техника.
        :param count: Количество.
        :param subdivision: Подразделение.
        """
        self.office_equipment = office_equipment
        self.count = count
        self.subdivision = subdivision


class Warehouse:
    """
    Склад
    """
    def __init__(self):
        self.items = []

    def take_office_equipment(self, office_equipment, count):
        """
        Метод принимает технику в подразделение 'Склад'
        :param office_equipment: Техника.
        :param count: Количество.
        """
        self.items.append(WarehouseItem(office_equipment, count, 'Склад'))

    def move_office_equipment(self, office_equipment, count, subdivision):
        """
        Метод перемещает технику со склада в указанное подразделение.
        :param office_equipment: Техника.
        :param count: Количество.
        :param subdivision: Подразделение.
        """
        for item in self.items:
            if item.office_equipment is office_equipment:
                if item.count > count:
                    item.count -= count
                    self.items.append(WarehouseItem(office_equipment,
                                                    count, subdivision))
                elif item.count == count:
                    item.subdivision = subdivision


class OfficeEquipment:
    """
    Офисная техника
    """
    price = NotNegativeInt('price')

    def __init__(self, type_equipment, brand, model, serial_number, color, price):
        """
        Конструктор
        :param type_equipment: Тип
        :param brand: Производитель
        :param model: Модель
        :param serial_number: Серийный номер
        :param color: Цвет
        :param price: Цена
        """
        self.type_equipment = type_equipment
        self.brand = brand
        self.model = model
        self.serial_number = serial_number
        self.color = color
        self.price = price


class Printer(OfficeEquipment):
    """
    Принтер
    """
    max_number_of_sheets = NotNegativeInt('max_number_of_sheets')

    def __init__(self, brand, model, serial_number, color,
                  price, paper_format, max_number_of_sheets):
        """
        Конструктор
        :param type: Тип
        :param brand: Производитель
        :param model: Модель
        :param serial_number: Серийный номер
        :param color: Цвет
        :param price: Цена
        :param paper_format: Формат бумаги
        :param max_number_of_sheets: Максимальное количество листов
        """
        super().__init__('Принтер', brand, model, serial_number, color, price)
        self.paper_format = paper_format
        self.max_number_of_sheets = max_number_of_sheets

    def __copy__(self):
        return Printer(self.brand, self.model, self.serial_number,
                       self.color, self.price, self.paper_format,
                       self.max_number_of_sheets)


class Scanner(OfficeEquipment):
    """
    Сканер
    """
    def __init__(self, brand, model, serial_number, color,
                 price, paper_format):
        """
        Конструктор
        :param type: Тип
        :param brand: Производитель
        :param model: Модель
        :param serial_number: Серийный номер
        :param color: Цвет
        :param price: Цена
        :param paper_format: Формат бумаги
        :param max_number_of_sheets: Максимальное количество листов
        """
        super().__init__('Сканер', brand, model, serial_number, color, price)
        self.paper_format = paper_format

    def __copy__(self):
        return Scanner(self.brand, self.model, self.serial_number,
                       self.color, self.price, self.paper_format)


class Xerox(OfficeEquipment):
    """
    Ксерокс
    """
    max_number_of_sheets = NotNegativeInt('max_number_of_sheets')

    def __init__(self, brand, model, serial_number, color,
                  price, paper_format, max_number_of_sheets):
        """
        Конструктор
        :param type: Тип
        :param brand: Производитель
        :param model: Модель
        :param serial_number: Серийный номер
        :param color: Цвет
        :param price: Цена
        :param paper_format: Формат бумаги
        :param max_number_of_sheets: Максимальное количество листов
        """
        super().__init__('Ксерокс', brand, model, serial_number, color, price)
        self.paper_format = paper_format
        self.max_number_of_sheets = max_number_of_sheets

    def __copy__(self):
        return Xerox(self.brand, self.model, self.serial_number,
                       self.color, self.price, self.paper_format,
                       self.max_number_of_sheets)


warehouse = Warehouse()
xerox = Xerox('HP', 'Laser Jet 2785', 'HP-LJ2785-0253',
              'Белый', 12500.5, 'A4', 500)
printer = Printer('Epson', 'DP-500', 'E-DP-500-7851',
                  'Чёрный', 24256.0, 'A4', 450)
scanner = Scanner('Epson', 'HD-Color-800', 'EHD-C800-GR',
                  'Серый', 16354.3, 'A4')
warehouse.take_office_equipment(xerox, 5)
warehouse.take_office_equipment(printer, 2)
warehouse.take_office_equipment(scanner, 1)
columns_length = [1, 3, 13, 6, 14, 4, 4, 6, 13]


def print_list():
    """
    Функция выводит на экран список техники
    """
    for index, item in enumerate(warehouse.items, 1):
        number_length = len(str(index))
        if number_length > columns_length[0]:
            columns_length[0] = number_length
        type_length = len(item.office_equipment.type_equipment)
        if type_length > columns_length[1]:
            columns_length[1] = type_length
        brand_length = len(item.office_equipment.brand)
        if brand_length > columns_length[2]:
            columns_length[2] = brand_length
        model_length = len(item.office_equipment.model)
        if model_length > columns_length[3]:
            columns_length[3] = model_length
        color_length = len(item.office_equipment.color)
        if color_length > columns_length[4]:
            columns_length[4] = color_length
        serial_number_length = len(item.office_equipment.serial_number)
        if serial_number_length > columns_length[5]:
            columns_length[5] = serial_number_length
        price_length = len(str(item.office_equipment.price))
        if price_length > columns_length[6]:
            columns_length[6] = price_length
        count_length = len(str(item.count))
        if count_length > columns_length[7]:
            columns_length[7] = count_length
        subdivision_length = len(item.subdivision)
        if subdivision_length > columns_length[8]:
            columns_length[8] = subdivision_length
    print(f' {"№":^{columns_length[0]}}'
          f' {"Тип":^{columns_length[1]}}'
          f' {"Производитель":^{columns_length[2]}}'
          f' {"Модель":^{columns_length[3]}}'
          f' {"Серийный номер":^{columns_length[4]}}'
          f' {"Цвет":^{columns_length[5]}}'
          f' {"Цена":^{columns_length[6]}}'
          f' {"Кол-во":^{columns_length[7]}}'
          f' {"Подразделение":^{columns_length[8]}}')
    for index, item in enumerate(warehouse.items, 1):
        print(f' {index:^{columns_length[0]}}'
              f' {item.office_equipment.type_equipment:<{columns_length[1]}}'
              f' {item.office_equipment.brand:^{columns_length[2]}}'
              f' {item.office_equipment.model:^{columns_length[3]}}'
              f' {item.office_equipment.serial_number:^{columns_length[4]}}'
              f' {item.office_equipment.color:^{columns_length[5]}}'
              f' {item.office_equipment.price:^{columns_length[6]}}'
              f' {item.count:^{columns_length[7]}}'
              f' {item.subdivision:^{columns_length[8]}} ')
    print('\n')


while True:
    print('"Добавить" - Добавить технику на склад')
    print('"Переместить" - Переместить технику')
    print('"Список" - Список техники')
    print('"Выйти" - Завершить работу программы')
    command = input('Введите команду: ')
    if command == 'Добавить':
        type_equipment = None
        while True:
            type_equipment = input('Выберите тип техники\n'
                        '"1" - Принтер\n'
                        '"2" - Сканер\n'
                        '"3" - Ксерокс\n'
                        ':')
            if type_equipment == '1' \
                    or type_equipment == '2' or type_equipment =='3':
                break
            else:
                print('Введите число соответствующее типу техники.')
        brand = input('Производитель: ')
        model = input('Модель: ')
        serial_number = input('Серийный номер: ')
        color = input('Цвет: ')
        price = None
        while True:
            try:
                price = validate_number(float(input('Цена: ')))
                break
            except ValueError:
                print('Введите число.')
            except NegativeNumber as error:
                print(error)
        paper_format = input('Формат бумаги: ')
        max_number_of_sheets = None
        if type_equipment != '2':
            while True:
                try:
                    max_number_of_sheets = validate_number(
                        int(input('Максимальное количество листов: ')))
                    break
                except ValueError:
                    print('Введите число.')
                except NegativeNumber as error:
                    print(error)
        count = None
        while True:
            try:
                count = validate_number(int(input('Количество: ')))
                break
            except ValueError:
                print('Введите число.')
            except NegativeNumber as error:
                print(error)
        if type_equipment == '1':
            warehouse.take_office_equipment(
                Printer(brand, model, serial_number, color,
                        price, paper_format, max_number_of_sheets),
                count)
        elif type_equipment == '2':
            warehouse.take_office_equipment(
                Scanner(brand, model, serial_number,
                        color, price, paper_format),
                count)
        elif type_equipment == '3':
            warehouse.take_office_equipment(
                Xerox(brand, model, serial_number, color,
                      price, paper_format, max_number_of_sheets),
                count)
    elif command == 'Переместить':
        print_list()
        index = None
        while True:
            try:
                index = validate_number(
                    int(input('Укажите проядковый номер техники: ')))
                if 0 < index < len(warehouse.items) + 1:
                    break
                else:
                    print('Введите порядковый номер техники.')
            except ValueError:
                print('Введите число.')
            except NegativeNumber as error:
                print(error)
        count = None
        while True:
            try:
                count = validate_number(int(input('Укажите количество: ')))
                if warehouse.items[index - 1].count >= count:
                    break
                else:
                    print(
                        f'{warehouse.items[index - 1].office_equipment.brand} '
                        f'{warehouse.items[index - 1].office_equipment.model} '
                        f'{warehouse.items[index - 1].office_equipment.color} '
                        f'- {warehouse.items[index - 1].count} шт.')
            except ValueError:
                print('Введите число.')
            except NegativeNumber as error:
                print(error)
        subdivision = None
        while True:
            subdivision = input('Укажите подразделение: ')
            if warehouse.items[index -1].subdivision == subdivision:
                print('Вы указали текущее подразделение.')
            elif subdivision == '':
                print('Вы не указали название подразделения.')
            else:
                break
        warehouse.move_office_equipment(
            warehouse.items[index - 1].office_equipment, count, subdivision)
    elif command == 'Список':
        print_list()
    elif command == 'Выйти':
        break
    else:
        print('Введите команду корректно.')
