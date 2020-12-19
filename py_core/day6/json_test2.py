# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import json

'''
把字典，转换为json串
'''
x = ''
json_text = '[{    "name": "ACME",  ' \
            '  "shares": 100,  ' \
            '  "price": 542.23,   ' \
            ' "gender": true,    "gender2": false,   ' \
            ' "hobby":["篮球" , "足球"],     "address":{      ' \
            '     "城市":"武汉",          ' \
            ' "省份": "湖北"}},{ "name": "adddd",  "shares": 100, ' \
            ' "price": 542.23, "gender": true,' \
            ' "gender2": false, "hobby":["篮球" , "足球"], "address":{ ' \
            '      "城市":"武汉",   "省份' \
            '": "湖北"' \
            ' }}]'

x = json.loads(json_text)

for i in x :
    print(i['name'])
