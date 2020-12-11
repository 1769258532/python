
class Person:
    def __new__(cls,*args,**kwargs) -> Any:
        print("-----创建白班----")
        return super().__new__(cls)

    def __init__(self,lastname,fistname,age) -> None:
        super().__init__()
        print("--------初始化对象-------")
        self.fistname=fistname
        self.lastname=lastname
        self.age=age
    @property
    def name(self):
        return self.lastname+self.lastname

    @name.setter
    def nama(self,fullname):
        self.fistname,self.lastname=fullname

    def __str__(self) -> str:
        return "我的名 字是{},年纪是{}".format(self.name,self.age)


if __name__ == '__main__':

    list=[]
    for i in range(4):
        x=Person("张"+str(i),"四",18)
        list.append(x)
    print(list)




