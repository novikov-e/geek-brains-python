"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения через
list и dict.
"""
month = input('Введите номер месяца: ')
seasons = {'Зима': ['1', '2', '12'],
           'Весна': ['3', '4', '5'],
           'Лето': ['6', '7', '8'],
           'Осень': ['9', '10', '11']}
season = None
complete = False
for key, value in seasons.items():
    for number in value:
        if month == number:
            season = key
            complete = True
            break
    if complete:
        break
print(season)
