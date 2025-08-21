# Stepick.org — Python: основы и применение
# 2. Cтандартные средства языка Python

import itertools
from datetime import date, timedelta
from simplecrypt import decrypt, DecryptionException
import os.path

# 2.1 Ошибки и исключения


def m_2_1_1():
    try:
        foo()
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ArithmeticError:
        print("ArithmeticError")
    except AssertionError:
        print("AssertionError")


def m_2_1_2():
    def parents(name):
        result = set()
        for parent in relations.get(name, []):
            result.add(parent)
            result |= parents(parent)
        return result

    def create_relations(count):
        data = {}
        for _ in range(count):
            name, *parents = input().split()
            if ":" in parents:
                data[name] = parents[1:]
            else:
                data[name] = []
        return data

    def call(count):
        calls = []
        for _ in range(count):
            name = input()
            if parents(name) & set(calls):
                print(name)
            else:
                calls.append(name)

    relations = create_relations(int(input()))
    call((int(input())))


def m_2_1_3():
    class NonPositiveError(Exception):
        pass

    class PositiveList(list):

        def append(self, object):
            if object > 0:
                return super().append(object)
            else:
                raise NonPositiveError("Only positive integers are allowed")


# 2.2 Работа с кодом: модули и импорт


def m_2_2_1():
    # from datetime import date, timedelta

    year, month, day = [int(x) for x in input().split()]
    days = timedelta(days=int(input()))

    d = date(year, month, day)
    result = d + days

    print(result.year, result.month, result.day)


def m_2_2_2():
    """
    для решения используется модуль pycryptodome и simplecrypt.py (src:
    https://github.com/andrewcooke/simple-crypt/blob/master/src/simplecrypt/__init__.py )

    bash:
    > python3 -m venv venv
    > source venv/bin/activate
    > pip install pycryptodome
    """
    with open("data/encrypted.bin", "rb") as file:
        encrypted = file.read()

    with open("data/passwords.txt", encoding="UTF-8") as file:
        for passwd in file:
            try:
                decrypted = decrypt(passwd.strip(), encrypted)
                print(decrypted.decode("utf-8"))
                break
            except DecryptionException:
                continue
            except Exception:
                continue


# 2.3 Итераторы и генераторы


def m_2_3_1():
    class multifilter:
        @staticmethod
        def judge_half(pos, neg):
            return pos >= neg

        @staticmethod
        def judge_any(pos, neg):
            return pos >= 1

        @staticmethod
        def judge_all(pos, neg):
            return neg == 0

        def __init__(self, iterable, *funcs, judge=judge_any):
            self.iterable = iterable
            self.funcs = funcs
            self.judge = judge

        def __iter__(self):
            for i in self.iterable:
                res = [f(i) for f in self.funcs]
                pos, neg = res.count(True), res.count(False)
                if self.judge(pos, neg):
                    yield i

    """
    #test
    def mul2(x):
        return x % 2 == 0

    def mul3(x):
        return x % 3 == 0

    def mul5(x):
        return x % 5 == 0

    a = [i for i in range(31)]
    print(
        list(multifilter(a, mul2, mul3, mul5))
        == [
            0,
            2,
            3,
            4,
            5,
            6,
            8,
            9,
            10,
            12,
            14,
            15,
            16,
            18,
            20,
            21,
            22,
            24,
            25,
            26,
            27,
            28,
            30,
        ]
    )
    print(
        list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))
        == [0, 6, 10, 12, 15, 18, 20, 24, 30]
    )
    print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)) == [0, 30])
    """


def m_2_3_2():

    def primes():
        num = 1
        while True:
            num += 1
            if num == 2 or all(num % div != 0 for div in range(2, int(num**0.5) + 1)):
                yield num

    # print(list(itertools.takewhile(lambda x: x <= 31, primes())))
    # print("[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]")


# 2.4 Работа с файловой системой и файлами


def m_2_4_1():
    input_file = "data/dataset_24465_4.txt"
    ouput_file = "data/result_2_4_1.txt"
    with open(input_file, encoding="UTF-8") as f, open(
        ouput_file, "w", encoding="UTF-8"
    ) as res:
        data = [line.strip() for line in f if line]
        res.write("\n".join(data[::-1]))


def m_2_4_2():
    # import os.path

    dir_name = "data/main"
    result = set(
        os.path.relpath(curentdir, "data")
        for curentdir, dirs, files in os.walk(dir_name)
        if any(file.endswith(".py") for file in files)
    )
    with open("data/result_2_4_2.py", "w", encoding="UTF-8") as f:
        f.write("\n".join(sorted(result)))


# 2.5 Работа с функциями: functools и лямбда-функции


def m_2_5_1():
    def mod_checker(x, mod=0):
        return lambda y: y % x == mod

    mod_3 = mod_checker(3)
    print(mod_3(3) == True)
    print(mod_3(4) == False)
    mod_3_1 = mod_checker(3, 1)
    print(mod_3_1(4) == True)


# 2.6 Стиль программирования: PEP 8 и документация
