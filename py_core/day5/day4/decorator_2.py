#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
  系统重构代码，执行业务函数1，2 ，需要认证  name = kevin  passwd = 123456
'''
def outer(name , password):

    def  business(fn):
        def  inner():
            if name == "kevin" and password == "123456":
                fn()
            else:
                pass
        return inner

    return business


@outer("kevin", "123456")
def foo1():
    ''''
    业务操作1
    '''
    print("---执行业务操作1----------------")
    pass


@outer("kevin", "123456")
def foo2():
    ''''
    业务操作1
    '''
    print("---执行业务操作2----------------")
    pass


if __name__ == '__main__':
    foo1()
    pass