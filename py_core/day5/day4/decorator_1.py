#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
  系统重构代码， 执行业务函数1，2 ，需要认证  name = kevin  passwd = 123456
'''
def business(name , password , method ):
    '''

    :param name:
    :param password:
    :param method:  业务函数名
    :return:
    '''

    if method.__name__ == "foo1":

        if name == "kevin" and password =="123456":
            foo1()
    elif method.__name__ == "foo2":
        if name == "kevin" and password =="123456":
            foo2()
    else:
        pass




def foo1():
    ''''
    业务操作1
    '''
    print("---执行业务操作1----------------")
    pass



def foo2():
    ''''
    业务操作1
    '''
    print("---执行业务操作2----------------")
    pass


if __name__ == '__main__':

    test_name = "kevin"

    password = "123456"

    business(name=test_name, password=password, method=foo1)

    pass