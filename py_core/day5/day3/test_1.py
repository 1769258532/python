#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
# import pytest



def  prinf():

    print("abc")
    return  1


def  test_1():

    r = prinf()

    assert  r == 1 ,  "断言失败"

#for test
if __name__ == '__main__':

    test_1() #第一个用例

    pass
