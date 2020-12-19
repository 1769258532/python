#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

def test1(*args):
    print(*args) #

test_data = [1,2,3]

test1(*test_data)

def test2(x , * , y , z , **kwargs): # *表示强制

    print(x, y , z, kwargs)
    pass

test2(1, y=1, z=2, c=3)