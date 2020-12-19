    #-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
函数，接收n个关键字参数, 在函数定义中只有一个** 参数，并且必须放最右边
'''
def test_1(*args , **kwargs):  # 可以接受任意的参数

    print(args)  #  元组
    print(kwargs)  #  一个字典
    pass

test_1("abc" , 10 , name="kevin" , age=19  )

