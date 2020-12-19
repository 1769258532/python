# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
1001 : 被0除

1002: 参数类型错误

1003： 消息内容过少

'''


class My_Exception(Exception):

    def __init__(self, error_code) -> None:
        self.error_code = error_code

    def __str__(self):
        return str(self.error_code)

if __name__ == '__main__':
    e = My_Exception("1001")

    print(e)

    pass
