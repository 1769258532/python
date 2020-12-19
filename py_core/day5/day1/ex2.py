#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
实现一个功能用户输入一个字符串，修该字符串中哪个位置的字符
，程序就会输出修改后的结果。比如用户输入：bugteacher.cn  位置6  替换字符- ，将会输出：bugte-cher.cn。

'''
#输入
text  = input("请输入一个字符串")
pos = int(input("请输入要替换的位置"))
value  = input("请输入替换字符")
#程序的处理
out = text[:pos - 1] + value + text[pos:]
#输出
print(out)




