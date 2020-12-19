
#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
继承的本质，是为了代码复用，

'''
from day4.person import Person


class Student(Person):

    def __init__(self, name, age , xh):
        super().__init__(name, age)
        # super(Student, self).__init__(name,age) # python2
        self.xh = xh

    def __str__(self) -> str:
        return "学生的名字叫{},学号{}".format(self.name, self.xh)

    # 使用一个名字相同的方法，覆盖超类的方法
    def talk(self , msg = "abc"):
        print("{}学生正在说话 {}".format(self.name, msg))
        pass


if __name__ == '__main__':
    s1 = Student(name="kevin", age=10, xh="10001")
    s1.talk()
    print(s1)

    pass
