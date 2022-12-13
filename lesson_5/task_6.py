"""
6. **Сформировать (не программно) текстовый файл. В нём каждая строка должна
описывать учебный предмет и наличие лекционных, практических и лабораторных
занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий
по нему. Вывести его на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re
from functools import reduce

school_subjects = {}

with open("task_6.txt", "r", encoding='utf-8') as input_file:
    for line in input_file:
        name_pattern = re.compile(r"(?P<name>[а-яёА-ЯЁ]+):")
        hours_pattern = re.compile(r"(?P<number_of_hours>[0-9]+)\(")
        name_matcher = name_pattern.findall(line)
        hours_matcher = hours_pattern.findall(line)
        hours = reduce(
            lambda first, second: int(first) + int(second),
            hours_matcher)
        school_subjects[name_matcher[0]] = hours

print(school_subjects)
