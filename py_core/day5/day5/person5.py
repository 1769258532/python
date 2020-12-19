# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
如果编程，写自己的类，不会使用类方法，或者静态方法

可以使用函数，替代。

'''

class Person:
    def __init__(self, firstname, lastname, age):  # 快捷键 ctr + o
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @classmethod #类方法，不需要创建对象
    def show(cls):
        print(cls)

        pass

    @staticmethod
    def show2(x , y):

        print("dddd")
        pass




if __name__ == '__main__':
    Person.show2(1,2)


