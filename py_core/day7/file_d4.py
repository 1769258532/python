#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
逐行读取
'''

# f = open("test_data.txt", encoding="utf8")
#
# for line in f:
#
#     print(line)
#
# f.close()

#上下文管理器

with open("test_data.txt", encoding="utf8") as f:
    for line in f:
        print(line)


