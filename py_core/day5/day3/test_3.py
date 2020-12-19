#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
带参函数
'''

def add( x,  y  = 1  ): # 函数定义中，位置参数，在默认值前面

    '''

    :param x:
    :param y:
    :return:
    '''

    return x + y

if __name__ == '__main__':
    add(1,2)
    add(1)
    add(x = 3, y =4)
    add(y = 5, x =3)



    pass


