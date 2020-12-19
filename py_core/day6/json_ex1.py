#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
使用json模块，解码字典对象，
创建学生对象。

'''
import json

from student import Student

json_data = '{ "studentNo": 1,"studentName": "陈超","age": 18}'

def fn(value):


    return Student(name=value['studentName'], age=value['age'] , xh=value['studentNo'])

x = json.loads(json_data,object_hook=fn)


x.talk()