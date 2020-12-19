# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

test_data = {

    "name": "wp",  # 数据项  item
    "age": 18

}
# 增加数据项， 修改数据
test_data.update(
    {
        "name": "zc",  # 数据项  item
        "age": 20,
        "address" : "武汉"

    }

)

print(test_data)
