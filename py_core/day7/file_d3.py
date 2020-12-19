#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
逐行读取
'''

f = open("test_data.txt", encoding="utf8")

for line in f.readlines(): # for line in f 也可以，f文件对象是一个可迭代对象

    print(line)

