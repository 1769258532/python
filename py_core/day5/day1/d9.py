#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
元组 , 不可变 和字符串
'''

x =  ( 1 ,2.4 ,"abc", ["hello", "world"], 5,)

print(type(x))

# x[-1] = 6 #无法修改，只能读取，切片读片段

# 如果元组中只有一个元素 必须加,

y = (1,)

print(type(y))

