#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
读取文件的内容
'''

file_path = r"G:\虫师\python\12_terms\12cs\day7\test_data.txt" #

f = open(file_path,encoding="utf8", mode="r") # 函数的返回值，是文件对象

content = f.read()

print(content)

f.close() #关闭
