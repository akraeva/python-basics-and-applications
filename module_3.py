# Stepick.org — Python: основы и применение
# 3. Применение Python: анализ текста

import csv
from xml.etree import ElementTree as et
import json
from sys import stdin
import re
import requests


# 3.1 Стандартные методы и функции для строк


def m_3_1_1():
    """
    Вашей программе на вход подаются три строки s, a, b,
    состоящие из строчных латинских букв. За одну операцию
    вы можете заменить все вхождения строки a в строку s на строку b.
    Например, s = "abab", a = "ab", b = "ba", тогда после выполнения
    одной операции строка s перейдет в строку "baba", после выполнения
    двух и операций – в строку "bbaa", и дальнейшие операции
    не будут изменять строку s.
    Необходимо узнать, после какого минимального количества операций
    в строке s не останется вхождений строки a. Если операций потребуется
    более 1000, выведите Impossible.
    Выведите одно число – минимальное число операций, после применения
    которых в строке s не останется вхождений строки a, или Impossible,
    если операций потребуется более 1000.
    """
    s, a, b = (input() for _ in range(3))
    for i in range(1000):
        if a in s:
            s = s.replace(a, b)
        else:
            print(i)
            break
    else:
        print("Impossible")


def m_3_1_2():
    """
    Вашей программе на вход подаются две строки s и t,
    состоящие из строчных латинских букв.
    Выведите одно число – количество вхождений строки t в строку s.
    """
    s, t = input(), input()
    count = 0
    start = 0
    while True:
        start = s.find(t, start)
        if start == -1:
            break
        count += 1
        start += 1

    print(count)


# 3.2  Регулярные выражения в Python


def m_3_2_1():
    """
    Вам дана последовательность строк. Выведите строки, содержащие
    "cat" в качестве подстроки хотя бы два раза.
    Примечание: Считать все строки по одной из стандартного потока
    ввода вы можете, например, так
    import sys
    """
    pattern = r"cat(.)*cat"

    for line in stdin:
        line = line.rstrip("\n")
        if re.search(pattern, line):
            print(line)


def m_3_2_2():
    """
    Вам дана последовательность строк.
    Выведите строки, содержащие "cat" в качестве слова.

    Примечание:
    Для работы со словами используйте группы символов b и B.
    Описание этих групп вы можете найти в документации.
    """

    pattern = r"\bcat\b"

    for line in stdin:
        line = line.rstrip("\n")
        if re.search(pattern, line):
            print(line)


def m_3_2_3():
    """
    Вам дана последовательность строк. Выведите строки, содержащие
    две буквы "z", между которыми ровно три символа.
    """

    pattern = r"z...z"

    for line in stdin:
        line = line.rstrip("\n")
        if re.search(pattern, line):
            print(line)


def m_3_2_4():
    """
    Вам дана последовательность строк.
    Выведите строки, содержащие обратный слеш.
    """

    pattern = r"\\"

    for line in stdin:
        line = line.rstrip("\n")
        if re.search(pattern, line):
            print(line)


def m_3_2_5():
    """
    Вам дана последовательность строк.
    Выведите строки, содержащие слово, состоящее из двух
    одинаковых частей (тандемный повтор).
    """

    pattern = r"\b(\w+)\1\b"

    for line in stdin:
        line = line.rstrip("\n")
        if re.search(pattern, line):
            print(line)


def m_3_2_6():
    """
    Вам дана последовательность строк.
    В каждой строке замените все вхождения подстроки "human"
    на подстроку "computer" и выведите полученные строки.
    """

    pattern = r"human"

    for line in stdin:
        result = re.sub(pattern, "computer", line.rstrip("\n"))
        print(result)


def m_3_2_7():
    """
    Вам дана последовательность строк.
    В каждой строке замените первое вхождение слова,
    состоящего только из латинских букв "a" (регистр не важен),
    на слово "argh".
    Примечание: Обратите внимание на параметр count у функции sub.
    """
    pattern = r"\b(a)+\b"

    for line in stdin:
        result = re.sub(
            pattern, "argh", line.rstrip("\n"), count=1, flags=re.IGNORECASE
        )
        print(result)


def m_3_2_8():
    """
    Вам дана последовательность строк.
    В каждой строке поменяйте местами две первых буквы в каждом слове,
    состоящем хотя бы из двух букв. Буквой считается символ из группы w.
    """

    pattern = r"\b(\w)(\w)(\w*)\b"
    replace = r"\2\1\3"

    for line in stdin:
        result = re.sub(pattern, replace, line.rstrip("\n"))
        print(result)


def m_3_2_9():
    """
    Вам дана последовательность строк. В каждой строке замените
    все вхождения нескольких одинаковых букв на одну букву.
    Буквой считается символ из группы w.
    Sample Input:
    attraction
    buzzzz
    Sample Output:
    atraction
    buz
    """

    pattern = r"(\w)\1+"
    replace = r"\1"

    for line in stdin:
        result = re.sub(pattern, replace, line.rstrip("\n"))
        print(result)


def m_3_2_10():
    """ "
    Примечание:
    Эта задача является дополнительной, то есть ее решение не
    принесет вам баллы.
    Задача сложнее остальных задач из этого раздела, и идея ее решения
    выходит за рамки простого понимания регулярных выражений как средства
    задания шаблона строки.
    Мы решили включить данную задачу в урок, чтобы показать, что регулярным
    выражением можно проверить не только "внешний вид" строки,
    но и заложенный в ней смысл.


    Вам дана последовательность строк.
    Выведите строки, содержащие двоичную запись числа, кратного 3.

    Двоичной записью числа называется его запись в двоичной системе счисления.

    Примечание 2:
    Данная задача очень просто может быть решена приведением
    строки к целому числу и проверке остатка от деления на три,
    но мы все же предлагаем вам решить ее, не используя приведение к числу.
    Sample Input:
    0
    10010
    00101
    01001
    Not a number
    1 1
    0 0
    Sample Output:
    0
    10010
    01001
    """


# 3.3 Обзорно об интернете: http-запросы, html-страницы и requests


def m_3_3_1(a, b):
    """
    Рассмотрим два HTML-документа A и B.
    Из A можно перейти в B за один переход, если в A есть ссылка на B,
    т. е. внутри A есть тег <a href="B">, возможно с дополнительными
    параметрами внутри тега.
    Из A можно перейти в B за два перехода если существует такой
    документ C, что из A в C можно перейти за один переход и из C в B
    можно перейти за один переход.
    Вашей программе на вход подаются две строки, содержащие url двух
    документов A и B. Выведите Yes, если из A в B можно перейти за два
    перехода, иначе выведите No.
    Обратите внимание на то, что не все ссылки внутри HTML документа
    могут вести на существующие HTML документы.
    """
    # import requests
    # import re
    # a, b = input(), input()
    b = b.replace("stepik.org", "stepic.org")
    data_a = requests.get(a)
    if not data_a.ok:
        return "No"
    pattern = r"<a [.]*href=[\'\"]([^\"\']+)"
    data_a_links = re.findall(pattern, data_a.text, flags=re.IGNORECASE)

    for c in data_a_links:
        data_c = requests.get(c)
        if data_c.ok:
            data_c_links = re.findall(pattern, data_c.text, flags=re.IGNORECASE)
            if b in data_c_links:
                return "Yes"
    return "No"

    """
    print(
        m_3_3_1(
            "https://stepik.org/media/attachments/lesson/24472/sample0.html",
            "https://stepic.org/media/attachments/lesson/24472/sample2.html",
        )
        == "Yes"
    )

    print(
        m_3_3_1(
            "https://stepik.org/media/attachments/lesson/24472/sample0.html",
            "https://stepik.org/media/attachments/lesson/24472/sample1.html",
        )
        == "No"
    )

    print(
        m_3_3_1(
            "https://stepik.org/media/attachments/lesson/24472/sample1.html",
            "https://stepik.org/media/attachments/lesson/24472/sample2.html",
        )
        == "Yes"
    )
    """


def m_3_3_2():
    """
    Вашей программе на вход подается ссылка на HTML файл.
    Вам необходимо скачать этот файл, затем найти в нем
    все ссылки вида <a ... href="..." ... > и вывести список
    сайтов, на которые есть ссылка.

    Сайтом в данной задаче будем называть имя домена вместе
    с именами поддоменов. То есть, это последовательность символов,
    которая следует сразу после символов протокола, если он есть,
    до символов порта или пути, если они есть, за исключением
    случаев с относительными ссылками вида
    <a href="../some_path/index.html">.
    Сайты следует выводить в алфавитном порядке.
    """

    def sites(data):
        pattern = r'<a[^>]+href=["\']([^"\']+)'
        hrefs = re.findall(pattern, data)
        res = []
        for href in hrefs:
            if href and not href.startswith((".", "/", "#", "?")):
                if "//" in href:
                    href = href[href.index("//") + 2 :]
                for smbl in "/:#?":
                    if smbl in href:
                        href = href[: href.index(smbl)]
                if "." in href:
                    res.append(href)
        return sorted(set(res))

    link = input()
    data = requests.get(link)
    print(*sites(data.text.lower()), sep="\n")

    """
    with open("data/3_3_2_data.txt") as f:
        test_data = f.read()
    print(" ".join(sites(test_data)) == "mail.ru neerc.ifmo.ru stepik.org www.ya.ru ya.ru")
    """


# 3.4 Распространённые форматы текстовых файлов: CSV, JSON


def m_3_4_1():
    """
    Вам дана частичная выборка из датасета зафиксированных преступлений,
    совершенных в городе Чикаго с 2001 года по настоящее время.
    Одним из атрибутов преступления является его тип – Primary Type.
    Вам необходимо узнать тип преступления, которое было зафиксировано
    максимальное число раз в 2015 году.
    """
    # import csv

    res = {}
    with open("data/Crimes.csv") as f:

        rows = csv.DictReader(f)
        for row in rows:
            if "2015" in row["Date"]:
                name = row["Primary Type"]
                res[name] = res.get(name, 0) + 1
    print(max(res, key=res.get))  # type: ignore # THEFT


def m_3_4_2():
    """
    Вам дано описание наследования классов в формате JSON.
    Описание представляет из себя массив JSON-объектов,
    которые соответствуют классам. У каждого JSON-объекта
    есть поле name, которое содержит имя класса, и поле parents,
    которое содержит список имен прямых предков.

    Пример:
    [{"name": "A", "parents": []},
     {"name": "B", "parents": ["A", "C"]},
     {"name": "C", "parents": ["A"]}]

    Эквивалент на Python:

    class A:
        pass

    class B(A, C):
        pass

    class C(A):
        pass

    Гарантируется, что никакой класс не наследуется от себя
    явно или косвенно, и что никакой класс не наследуется явно
    от одного класса более одного раза.
    Для каждого класса вычислите предком скольких классов он
    является и выведите эту информацию в следующем формате.
    <имя класса> : <количество потомков>
    Выводить классы следует в лексикографическом порядке.
    """
    # import json

    def get_all(name):
        res = set()
        for child in parents.get(name, []):
            res.add(child)
            res.update(get_all(child))
        return res

    parents = {}
    data = json.loads(input())
    for row in data:
        parents.setdefault(row["name"], [])
        for parent in row["parents"]:
            parents.setdefault(parent, []).append(row["name"])

    childrens = {parent: get_all(parent) for parent in parents}
    print(
        *(f"{key} : {len(value)+1}" for key, value in sorted(childrens.items())),
        sep="\n",
    )


# 3.5 API


def m_3_5_0():
    # import requests
    # import json

    api_key = "9672b1fc951386d319b831561008cdc0"
    city_name = "Moscow"
    api_citi_url = "https://api.openweathermap.org/geo/1.0/direct"
    city_params = {"q": city_name, "limit": 5, "appid": api_key}

    coordinates = requests.get(api_citi_url, city_params).json()[0]
    lat, lon = coordinates["lat"], coordinates["lon"]

    api_weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        "lat": lat,
        "lon": lon,
        "lang": "ru",
        "units": "metric",
        "appid": api_key,
    }
    data = requests.get(api_weather_url, weather_params).json()
    weather = data["main"]["temp"]
    print(f"Сейчас температура в городе {data['name']} — {weather}˚C")


def m_3_5_1():
    """
    В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
    Вам дается набор чисел. Для каждого из чисел необходимо узнать,
    существует ли интересный математический факт об этом числе.

    Для каждого числа выведите Interesting, если для числа существует
    интересный факт, и Boring иначе. Выводите информацию об интересности
    чисел в таком же порядке, в каком следуют числа во входном файле.

    Пример запроса к интересному числу:
    http://numbersapi.com/31/math?json=true

    Пример запроса к скучному числу:
    http://numbersapi.com/999/math?json=true

    Пример входного файла:
    31
    999
    1024
    502

    Пример выходного файла:
    Interesting
    Boring
    Interesting
    Boring
    """

    # import json
    # import requests

    data_file = "data/dataset_24476_3.txt"  # "data/data_3_5_1.txt"
    api_link = "http://numbersapi.com/"
    param = "/math?json=true"
    with open(data_file, encoding="UTF-8") as f:
        for num in f:
            link = api_link + num.rstrip() + param
            res = requests.get(link).json()
            print("Interesting" if res["found"] else "Boring")


def m_3_5_2():
    """
    В этой задаче вам необходимо воспользоваться API сайта artsy.net
    API проекта Artsy предоставляет информацию о некоторых деятелях
    искусства, их работах, выставках. В рамках данной задачи вам понадобятся
    сведения о деятелях искусства (назовем их, условно, художники).
    Вам даны идентификаторы художников в базе Artsy.
    Для каждого идентификатора получите информацию о имени художника
    и годе рождения. Выведите имена художников в порядке неубывания
    года рождения. В случае если у художников одинаковый год рождения,
    выведите их имена в лексикографическом порядке.

    Алгоритм (работал на 2-09-2026):
        1.	Регистрируешься на Artsy Developers https://developers.artsy.net/
        2.	Авторизуешься в браузере и переходишь на любую страницу API, например:
        https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4
        3.	В инструментах разработчика находишь ключ с именем _gravity_secure_session

    Примечание:
    В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

    Пример входных данных:
    4d8b92b34eb68a1b2c0003f4
    537def3c139b21353f0006a6
    4e2ed576477cc70001006f99

    Пример выходных данных:
    Abbott Mary
    Warhol Andy
    Abbas Hamra
    """

    # import requests

    gravity_secure_session = r"put your _gravity_secure_session cookie here"
    cookie = {
        "_gravity_secure_session": gravity_secure_session,
        "signed_in": "true",
    }

    file_name = "data/data_3_5_2.txt"  # for tests
    with open(file_name, encoding="utf-8") as f:
        artist_ids = [line.strip() for line in f]

    artists = []
    for artist_id in artist_ids:
        url = f"https://api.artsy.net/api/artists/{artist_id}"
        data = requests.get(url, cookies=cookie).json()
        artists.append(data)

    result = sorted(
        artists, key=lambda artist: (int(artist["birthday"]), artist["sortable_name"])
    )
    for artist in result:
        print(artist["sortable_name"])


# 3.6 XML, библиотека ElementTree, библиотека lxml


def m_3_6_1(data):
    """
    Вам дано описание пирамиды из кубиков в формате XML.
    Кубики могут быть трех цветов:
    красный (red), зеленый (green) и синий (blue).
    Для каждого кубика известны его цвет, и известны кубики,
    расположенные прямо под ним. Введем понятие ценности для
    кубиков. Самый верхний кубик, соответствующий корню XML
    документа имеет ценность 1. Кубики, расположенные прямо
    под ним, имеют ценность 2. Кубики, расположенные прямо под
    нижележащими кубиками, имеют ценность 3. И т. д.
    Ценность цвета равна сумме ценностей всех кубиков этого цвета.
    Выведите через пробел три числа:
    ценности красного, зеленого и синего цветов.
    """
    # from xml.etree import ElementTree as et
    data = input()
    result = {"red": 0, "green": 0, "blue": 0}
    root = et.fromstring(data)
    value = 1
    queue = [root]
    while queue:
        children = []
        for element in queue:
            color = element.attrib["color"]
            result[color] += value
            children.extend(list(element))
        queue = children
        value += 1

    return f"{result['red']} {result['green']} {result['blue']}"


# test_data = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
# print(m_3_6_1(test_data) == "4 3 1")
