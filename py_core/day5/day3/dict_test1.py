#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

test_data = {} #  空字典

#向字典中，增加内容

test_data["name"] = "kevin"

print(test_data)

value = test_data.setdefault( "address" , "武汉")

#修改
if value.startswith("武汉"):

    # test_data["address"] = value + str(1) # 修改
    test_data.update({

        "address" : value +str(1)
    })

print(test_data)

#获取所有的数据项
for k , v in test_data.items():

    print(k , v)

#删除某一项
del test_data["name"]


print(test_data)

#清空字典
# test_data.clear()








