#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
1. 类里有  __iter__，那么这个类的对象，是可迭代的对象
2. __iter__方法，必须返回一个迭代器
'''
class School:

    def __init__(self , name, addr) -> None:
        '''
        :param name: 学校名字
        :param addr:  学校地址
        '''
        self.student_nos = [1,2,3]
        self.name = name
        self.addr = addr


    # 返回一个迭代器
    def __iter__(self):

        return iter(self.student_nos)

if __name__ == '__main__':
    school = School(name = "武大", addr="武汉")
    for i in school: #可迭代对象
        print(i)


    pass
