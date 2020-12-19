#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
   bugteacher.cn
   输入 位置  3 到  10 ，换成一个新的串 ， “replace”
   输出一个替换后的新字符串.
'''
text = "bugteacher.cn"
start, end , replace = int(input("输入起始位置")),\
                       int(input("输入终止位置")),\
                       input("输入替换字符串")

#业务逻辑
r = text[:start - 1]  + replace + text[end:] #索引可以是变量


print(r)


