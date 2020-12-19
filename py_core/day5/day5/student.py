#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
继承的本质，是为了代码复用，

'''
from Tools.scripts.which import msg

from day5.day5.person import Person
from day7.exception import My_Exception


class Student(Person):

    def __init__(self, name, age , xh):
        super().__init__(name, age)
        # super(Student, self).__init__(name,age) # python2
        self.xh = xh

    # def __str__(self) -> str:
    #     print( "学生的名字叫{},学号{}".format(self.name, self.xh))

    # 使用一个名字相同的方法，覆盖超类的方法
    def talk(self , msg = "abc"):


        return  "{}学生正在说话 {}".format(self.name, msg)



if __name__ == '__main__':
    s1 = Student(name="kevin", age=10, xh="10001")


    print(s1.talk)


    pass
