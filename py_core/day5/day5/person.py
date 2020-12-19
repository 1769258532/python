# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
类是对象的模板， 对象是类的实例。
'''
from typing import Any
import json


class Person(object):

    city = "武汉" #类变量 ，所有对象，共有的属性

    def __new__(cls, *args,**kwargs):
        print(cls)
        print("----------创建一个白板对象")

        return super().__new__(cls)

    # 初始化 , 魔术方法，当我们创建一个对象的时候，由python，帮我们自动调用
    # 第一个参数，代表对象本身，由python自动传入
    # 初始化方法，没有返回值
    def __init__(self, name, age):  # 快捷键 ctr + o
        print("----------------初始化对象-------------------")
        self.name = name
        self.age = age


    # 实例方法，由对象去调用，谁调用，self表示谁。
    def talk(self):
        print("{}正在说话".format(self.name))
        pass

    def save_to_db(self):
        '''
        保存。用户名和年纪到数据库
        :return:
        '''

        pass

    def save_as_json(self):
        '''
        保存用户名和年纪到文件
        :return:
        '''

        pass


if __name__ == '__main__':
    s1 = Person("kevin", 19)
    s2 = Person("kevin2", 20)

    # s1.talk()
    # s2.talk()

    print(s1.talk())
    print(s2.city)


    pass
