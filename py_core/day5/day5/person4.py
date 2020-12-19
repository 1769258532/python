# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
类是对象的模板， 对象是类的实例。
'''

class Person:
    def __init__(self, firstname, lastname, age):  # 快捷键 ctr + o
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @property
    def name(self):
        return self.firstname + self.lastname

    @name.setter
    def name(self, fullname):
        self.firstname, self.lastname = fullname

    def talk(self):
        print("{}正在说话".format(self.name))
    '''
    1. print打印对象的时候。触发
    2. format对象的触发
    3. 调用str（）
    4. 主动 o.__str__()
    '''
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, o) -> bool:
        return self.name == o.name

    def __str__(self) -> str:
        return "我的名字叫{}, 年纪是{}".format(self.name, self.age)

    def __repr__(self) -> str:
        return "我的名字叫{}, 年纪是{}".format(self.name, self.age)


if __name__ == '__main__':
    s1 = set()
    for i in range(4):
        x = Person("张", "三", 19)
        s1.add(x)
    print(s1)

