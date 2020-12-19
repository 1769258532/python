#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
1. 替换工作
'''


def foo(fn):

    print("0000000000000000000000000000000000000000000000000")
    return  "hello"


@foo
def add(x, y):
    return x + y

print(add)

