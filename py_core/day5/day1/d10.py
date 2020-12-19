#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

class efg:
    '''
    字典
    '''
    # 字典 key: value  ，数据在value部分， 可变对象
    test_data = {

        "name" :"wp",  # 数据项  item
        "age": 18

    }

    print(test_data['age']) # 会用这个

    # print(test_data.get("address")) # 当key不存在的时候，返回None值

    #修改

    test_data["age"] = 20

    print(test_data)

    #删除
    del test_data['age']

    print(test_data)

    #增加一个数据项

    test_data["address"] = "湖北省武汉市"

    print(test_data)


