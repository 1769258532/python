#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
import time
'''
统计： 函数的调用执行时间
'''
def timethis(fn):
    def inner(*args, **kwargs):

        print("----开始调用函数-----")
        start = time.time()
        fn(*args,**kwargs)
        end = time.time()
        print("----函数调用结束-----，执行时间{}s".format(end -start))


    return inner

@timethis
def foo1(name, password):
    # if name == "kevin" and password == "123456":
        ''''
        业务操作1
        '''
        time.sleep(1)
        print("---执行业务操作1----------------")
        pass

@timethis
def foo2(name, password):
    # if name == "kevin" and password == "123456":
        ''''
        业务操作2
        '''
        time.sleep(3)
        print("---执行业务操作2----------------")
        pass

@timethis
def foo3():
    print("---执行业务操作3----------------")


if __name__ == '__main__':

    foo3()

    pass