#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
写入数据到文件

'''

f = open("abc.txt", encoding="utf-8")

f.read()

if f.closed:
    print("关闭了")

f.close()

