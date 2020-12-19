#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
练习： test_data2 = [ 1 ,2.4 ,"abc", ["hello", "world"], 5] #
1. 把world  读取出来
2. 把world  替换为 [ "a", "b"]
'''
test_data2 = [ 1 ,2.4 ,"abc", ["hello", "world"], 5 ,]

#1
x = test_data2[-2]
print(x[-1]) # 读取
x[-1] = ["a" , "b"] #修改
print(test_data2)

