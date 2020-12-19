#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

import json
'''
把字典，转换为json串
'''
test_data = {

    'name': 'ACME',
    'shares': 100,
    'price': 542.23

}

text = json.dumps(test_data, indent=8) # 把python对象，转换为json文本


print(type(text))

