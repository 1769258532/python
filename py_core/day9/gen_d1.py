#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
def gen():

    print("abc")

    for i in range(3):
        yield i
        print("efg")


#返回一个生成器
generator1 = gen() #生成器也是迭代器
print(next(generator1))
print(next(generator1))
print(next(generator1))




