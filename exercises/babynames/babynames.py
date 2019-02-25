#!/usr/bin/python3




"""Упражнение "Детские имена"

ЗАГС г. Москвы ведет статистику детских имен. На сайте этой организации 
публикуется статистика наиболее популярных имен по году рождения ребенка.

Файлы для этого упражнения находятся в файлах "babynames_boys.html" и 
"babynames_girls.html". Они содержат сырой HTML-код, подобный тому, 
что вы можете увидеть на официальном сайте ЗАГСа Москвы по адресу
http://zags.mos.ru/stat/imena/.

Взгляните на HTML и подумайте о том, как вы можете извлечь данные из него
при помощи регулярных выражений.

-= 1 часть =-

1. Создайте функцию extract_names(filename), которая принимает в качестве 
аргумента имя файла и возвращает данные из него в виде словаря вида:
babynames = {
'София, Софья': ['3841 (6,0%)*', '3668 (6,2%)', '2127 (4,8%)', 
    '826 (2,4%)', '193 (0,4%)',],
'Виктория': ['2219', '1994', '1829', '1076', '1033'],
...
}
Словарь использует в качестве ключа имя ребенка, а в качестве значения -
список, содержащий количесво детей, названных этим именем в соотв. году.  
Для упрощения задачи используйте строки в том виде, в котором они содержатся 
в HTML-файле.

2. Создайте функцию print_names(). Функция получает в качестве аргумента 
словарь babynames с данными вида ключ/список (описание словаря см. выше). 

Затем:

1. Запрашивает у пользователя интересующий его год (желательно вывести список 
    возможных вариантов и попросить ввести данные заново, если по указанному 
    году нет данных).

2. Выводит на печать данные в алфавитном порядке имен:
    Александра 1683
    Алина 837
    Алиса 1239
    Алёна, Алена 658
    Амина 243
    Анастасия 3055 (5,1%)
    ...

Подсказка: создайте служебный список с годами рождения: 
years = ['2012', '2010',...].
С его помощью вам будет проще определять позицию данных по году в списке 
словаря babynames.

Совет: удобнее всего писать программу, разбивая ее на серию небольших этапов,
выводя на печать результаты каждого шага. 

Вот некоторые предлагаемые основные этапы:

- Получите текст из файла и выведите его в консоль
- Сделайте проверку на существование файла. Если файл не существует - 
    сообщите об ошибке пользователю и завершите программу с флагом 
    ошибки sys.exit(1)
- Напишите регулярное выражение, выбирающее данные из таблицы, и выведите 
    эти данные в консоль в виде сырого списка
- Обработайте полученный список, удалив из каждой строки лишние пробелы 
    и символы пореноса строки с помощью метода str.strip() и выведите его в 
    консоль. (Подсказка: для обработки списков удобно использовать функцию map)
- Преобразуйте полученные данные в словарь заданной структуры и выведите 
    его в консоль. Если словарь получен - верните его функцией return и 
    переходите к опредению функции вывода print_names()

- Напишите функцию, запрашивающую данные у пользователя:
- Если пользователь ввел символ 'q' - выйдите из программы с кодом успешного 
    завершения sys.exit(0)
- Если введеного года нет в служебном списке years - 
    сообщите пользователю об этом, выведите список созможных вариантов 
    и завершите программу
- Если год есть в списке - выведите данные по этому году, сортируя словарь 
    по имени ребенка


-= 2 часть (дополнительная) =-

1. Усложненните функцию extract_names(filename). Пусть теперь она возвращает 
словарь следующего вида:
babynames = {
    'София, Софья': {
        2012: [3841, 6.0]', 
        2010: [3668, 6.2]',
        2005: [2127, 4.8]',
        2000: [826, 2.4]',
        1990: [193, 0.4]',
    },
    'Виктория': {
        2012: [2219, None],
        2010: [1994, None],
        2005: [1829, None],
        2000: [1076, None],
        1990: [1033, None],
    },
    ...
}
Словарь использует в качестве ключа имя ребенка, а в качестве значения -
еще один словарь, содержащий список, первый элемент которого содержит 
количество детей, а второй - данные в процентах, полученные из файла
(используйте None, если поле таблицы в файле не содержит процентных данных).

2. Функция print_names() работает аналогичным образом, но выдача сортируется
теперь по кол-ву детей и форматируется следующим образом:

София, Софья    3841   6,0%
Мария, Марья    3735   5,8%
...
Виктория        2219
Полина          2051
...

3. Пусть функция print_names() теперь запрашивает данные в цикле,
чтобы дать пользователю возможность получить выборку за разные годы.
В конце каждой итерации спрашивайте пользователя, хочет ли он продоожить работу:
Продолжить? (y/n)
Если введено 'n' - выйдите из программы.
"""

import re
import os
import urllib.request
import urllib.parse
import sys


sys.argv[0] = 'babynames_boys.html'

def extract_names(filename):

    """
    Получает имя файла. 
    Возвращает данные из файла в виде словаря:
    {
    'София, Софья': ['3841 (6,0%)*', '3668 (6,2%)', '2127 (4,8%)', 
        '826 (2,4%)', '193 (0,4%)',],
    'Виктория': ['2219', '1994', '1829', '1076', '1033'],
    ...
    }

    При написании регулярных выражений удобно держать перед глазами копию
    анализируемого текста. Вот как выглядит HTML-код в файле 
    babynames_girls.html:

    <tr> <td width="66"> 
        1
    </td> <td width="151"> 
        София, Софья 
    </td> <td width="85"> 
        3841 (6,0%)* 
    </td> <td width="104"> 
        3668 (6,2%) 
    </td> <td width="94"> 
        2127 (4,8%) 
    </td> <td width="104"> 
        826 (2,4%) 
    </td> <td width="104"> 
        193 (0,4%) 
    </td> </tr>

    """
    # +++ваш код+++


    real_dir = os.getcwd()                                                                                                             #передаём дирректорию в которой сейчас находимся
    real_way = str(os.path.abspath(os.path.join(real_dir, filename)))
    ufile = urllib.request.urlopen('file:///' + real_way)
    html = ufile.read().decode('utf 8')
    g5 = re.findall(r'<td width="104|94|90">\s*?(\w.*?)\s*?</td>', html)  # последующие значения
    g3 = re.findall(r'<td width="151|177">\s*?([йцукенгшщзхъфывапролджэячсмитьбюёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ, ]*?)\s*?</td>', html)   # имена
    g4 = re.findall(r'<td width="85|76">\s*?(\w.*?)\s*?</td>', html)                                                                       # первое значение
    result = {}
    result[g3[0]] = g4[0], g5[0], g5[1], g5[2], g5[3]                                                                                   #присвоили первые значения массиву
    for d in range(4, 200, 4):
        result[g3[int(d/4)]] = g4[int(d/4)], g5[d], g5[d + 1], g5[d + 2], g5[d + 3]
    years = ['2012', '2010', '2005', '2000', '1990']
    year_dict = {}
    for key in result:
        for y in range(5):                                                                                                             # создаём новые словари в которые записываем год как ключ , и количество детей в этот год
            year_dict[years[y]] = result[key][y]
        result[key] = year_dict
        year_dict = {}
    print(result)
    return result



def print_names(new_dict):                         #сортировка по количеству детей
    year = input("2012, 2010, 2005, 2000, 1990")
    andict = new_dict
    childlist = []                                                                                  # создаём пусток список для детей
    for key in andict:
        number = int(((andict[key][year]).split())[0])                                              # das
        childlist.append(tuple((key, number,)))                                                     # записываем имя и количество детей в указанный ранне список
    sorted_childlist = (sorted(childlist, key=lambda student: student[1], reverse=True))            # сортируем список по количеству детей
    for child in sorted_childlist:
        print(child)
    work = input("Do you want continue work? Press y if yes,else n")
    if work == "y":
        print_names(new_dict)
    else:
        sys.exit("Have a good day")

def main():
    # Код разбора командной строки
    # Получим список аргументов командной строки, отбросив [0] элемент, 
    # который содержит имя скрипта

    filename = input("filename")
    babynames = extract_names(filename)
    print_names(babynames)

  
if __name__ == '__main__':
    main()