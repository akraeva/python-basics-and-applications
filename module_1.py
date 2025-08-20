# Stepick.org — Python: основы и применение
# 1. Базовые принципы языка Python


# 1.1 Введение


def m_1_1():
    print(sum(int(input()) for _ in range(int(input()))))


# 1.2 Модель данных: объекты


def m_1_2():
    print(len(set(id(obj) for obj in (objects))))


# 1.3 Функции и стек вызовов


def m_1_3_1():
    def closest_mod_5(x):
        if x % 5 == 0:
            return x
        y = 5 * (x // 5 + 1)
        return y


def m_1_3_2():
    def combination(n, k):
        if k == 0:
            return 1
        if k > n:
            return 0
        return combination(n - 1, k) + combination(n - 1, k - 1)

    arg_n, arg_k = map(int, input().split())
    print(combination(arg_n, arg_k))


# 1.4 Пространства имён и области видимости


def m_1_4_1():
    spaces = {"global": "None"}
    vars = {"global": set()}

    for _ in range(int(input())):
        request, namespace, data = input().split()
        if request == "create":
            spaces[namespace] = data
            vars[namespace] = set()
        elif request == "add":
            vars[namespace].add(data)
        elif request == "get":
            while namespace != "None":
                if data in vars[namespace]:
                    print(namespace)
                    break
                namespace = spaces[namespace]
            else:
                print("None")


# 1.5 Введение в классы


def m_1_5_1():
    class MoneyBox:
        def __init__(self, capacity):
            self.capacity = capacity

        def can_add(self, v):
            return self.capacity >= v

        def add(self, v):
            self.capacity -= v


def m_1_5_2():
    class Buffer:
        def __init__(self):
            self.nums = []

        def add(self, *a):
            for num in a:
                self.nums.append(num)
                if len(self.nums) == 5:
                    print(sum(self.nums))
                    self.nums.clear()

        def get_current_part(self):
            return self.nums


# 1.6 Наследование классов


def m_1_6_1():
    def is_anc(des, anc):
        if des == anc:
            return True
        if anc in classes[des]:
            return True
        for parent in classes[des]:
            if is_anc(parent, anc):
                return True
        return False

    classes = {}
    for _ in range(int(input())):
        name, *ancs = input().split(" : ")
        classes[name] = [anc for anc in ancs[0].split()] if ancs else []

    for _ in range(int(input())):
        a, d = input().split()
        print("Yes" if is_anc(d, a) else "No")


def m_1_6_2():
    class ExtendedStack(list):
        def sum(self):
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 + top2)

        def sub(self):
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 - top2)

        def mul(self):
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 * top2)

        def div(self):
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 // top2)


def m_1_6_3():
    # import time
    class LoggableList(list, Loggable):
        def append(self, object):
            super().append(object)
            self.log(object)
