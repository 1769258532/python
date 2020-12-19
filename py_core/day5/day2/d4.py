#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
in  not in  成员运算符
'''


x = r'<script src="https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/js/s_super_index-855fcfd82e.js"></script>'
#
if "superman" in x:
    print("测试通过")



# list1 = ["abc" , 'efg' , "hello"]
#
# if "abc" in list1:
#
#     print("pass")

# value = {
#     "name" : "kevin"
# }
#
# key = "name"
# if  key in value:
#     print(value[key])


x = 1
y = 2

z = x + y * 3  / y == 1 <= 2 ** 3 % 2

print(z)
