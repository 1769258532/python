#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
闭包函数的特点
1。 在其他函数的内部定义
2.  访问外部函数的局部变量
3.  外部函数，必须返回这个内部函数

如果函数对象，有__closure__ 有值
'''
n = 9

def outer(x):
    y = 1 # outer函数里，定义的一个局部变量

    def inner(): # 闭包函数

        print(n)
        pass

    return inner


f = outer(1)


f()







