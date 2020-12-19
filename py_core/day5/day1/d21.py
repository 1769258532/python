#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
排序 1 . sort() 2 .sorted()
更多读数据，
'''
test_datas = [ 3, 2, 1, 0 ]
#
# test_datas.sort() #  方法
#
# print(test_datas)

r = sorted(test_datas) # r是对原列表，排序后的，新的列表

print(r)

assert  r is not test_datas , ""



