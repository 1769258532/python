#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
成员运算符  in   & not in
'''
#字符串
test_data = "hello,王盼"

print( "王盼"  in test_data)


#列表
test_data = ("kevin" , "eric" )

print( "kevin" in test_data)

#字典
test_data2 = {

    "name": "wp",  # 数据项  item
    "age": 18

}

if "name" in test_data2:
    print("success")



