#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
# 字典
stu = {
    "studentNo": "001",
    "studentName": "陈超",
    "phone": "1212312",
    "address": "武汉",
    "bornDate": "2020/9/8",
    "gradeId": 3
}
stu2 = {  k : v    for k, v  in stu.items() if k.startswith("s")}
print(stu2)
