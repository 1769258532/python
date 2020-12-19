# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
上下文管理器
'''
class Context:

    def __init__(self, file_name) -> None:
        self.fp = open(file_name, encoding="utf8")

    def __enter__(self):
        print("adddddd")
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
        print("关闭文件")


with Context("test_data.txt") as c:
    content = c.read()

    print(content)
