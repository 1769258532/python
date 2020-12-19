# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
列表推导式
0- 1000 ，数的列表
'''
list1 = [(i ,j) for i in range(1001)  for j in range(10) if j != 0]
print(list1)


