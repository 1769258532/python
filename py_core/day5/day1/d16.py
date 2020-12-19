#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
身份运算符 , 不可变数据类型，在内存中，只保存一份，数字，字符串，元组
is 用来比较2个变量的内存地址，
id()内置函数可以查看变量的内置地址
'''

# x = 1
#
# y = 1
#
# # print( x  == y ) #
# print( x  is y ) # 比较内存地址

# x = (1,)
#
# y = (1,)
#
# print(x is y) #比较内存地址

# x = "helllo"
#
# y = "helllo"
#
# print(x is y) #比较内存地址

x = [1,2,3]
x1 = [1,2,3]
x2 = [3,2,1]

print( id(x) , id(x1) , id(x2))

print( x == x2)

