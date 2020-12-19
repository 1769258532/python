#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
# 列表的定义 ，容器类型 ， 有序
test_data = [ 1 ,2 ,3, 4, 5] #
#列表可以包含任意的python数据类型
test_data2 = [ 1 ,2.4 ,"abc", ["hello", "world"], 5] #

#列表访问
x = test_data2[-2]

print(x)

#列表的切片
y = test_data2[:4]

print(y)

#重点：列表切片可以赋值
#列表是可变对象，可以修改元素的值，字符串是不可变对象，只能切片读，或者索引读取，无法修改

test_data2[:3] = ["a" , "b" , "c"]
print(test_data2)




