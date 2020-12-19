    #-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
for in 循环
'''

test_datas = [ 1 , 2, 3, 4 ]

# for i in test_datas: #   in 列表，元组
#     if i == 3:
#         break #完全跳出循环
#     print(i)

for i in test_datas: #   in 列表，元组
    if i == 3:
        continue # 终止本次循环，接着执行下一次迭代
    print(i)

# i = 0
#
# while i < 4  :
#     print(test_datas[i])
#     i += 1

