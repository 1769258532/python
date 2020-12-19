# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
迭代器 和可迭代对象
1. 列表，元组，字符串，都是可迭代的
'''
list1 = [1, 2, 3]

x1 = iter(list1) # 把可迭代对象。转换为迭代器

print(next(x1))
print(x1.__next__())
print(next(x1))



