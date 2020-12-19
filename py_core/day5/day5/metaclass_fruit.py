# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
任何类，默认是 type 类型的对象
'''


class efg(type):
    # cls 正在创建的类型本身
    # what 代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, what, bases=None, attr: dict = None):
        attr["chandi"] = "武汉"  # 类变量
        saved = {}
        for k, v in attr.items():
            if hasattr(v, "__call__") and k != "__init__":
                saved[k] = v
        for k, v in saved.items():
            attr.pop(k)

        # 新字典
        saved = {k + "_001": v for k, v in saved.items()}
        attr.update(saved)
        return super().__new__(cls, what, bases, attr)  # 真正创建类型对象本身


class _Fruit(metaclass=efg):

    def __init__(self, name, taste) -> None:
        self.__name = name
        self._taste = taste

    # 对客户公开的，接口函数
    def getName(self):
        return "水果的名字是{}".format(self.__name)

    def info(self):
        pass


if __name__ == '__main__':
    f = _Fruit("苹果", "甜")

    print(f.getName())

    # print(dir(_Fruit))

    # print(f.chandi)
