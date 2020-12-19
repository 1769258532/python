# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
  系统重构代码， 执行业务函数1，2 ，需要认证  name = kevin  passwd = 123456
  1. 打上@function ,会替换原有的函数为 business函数的返回值
'''
def business(fn):
    def inner(name, password):
        if name == "kevin" and password == "123456":
            fn(name, password)
        else:
            pass

    return inner

@business
def foo1(name, password):
    # if name == "kevin" and password == "123456":
        ''''
        业务操作1
        '''
        print("---执行业务操作1----------------")
        pass

@business
def foo2(name, password):
    # if name == "kevin" and password == "123456":
        ''''
        业务操作1
        '''
        print("---执行业务操作2----------------")
        pass


if __name__ == '__main__':
    foo1("kevin111", "123456")

