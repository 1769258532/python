'''
  系统重构代码， 执行业务函数1，2 ，需要认证  name = kevin  passwd = 123456
'''
def outer(name,passwd):

    def inner(fn):

        if name=="kevin" and passwd=="123456":
            fn()
        else:
            pass
        return inner
    return outer


@outer("kevin","123456")
def foo():
    print("业务操作")
if __name__ == '__main__':
    foo()
    pass






