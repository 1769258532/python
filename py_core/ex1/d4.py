class efg(type):

    def __new__(cls,what,bases=None,attr=None) :
        attr["chandi"]="武汉"
        for k,v in attr.

        return type.__new__(cls,what,bases,attr)
class _Fruit(metaclass=efg):
    def __init__(self,name,taste) -> None:
        self.__name=name #私有的
        self._taste=taste #不能被from导入
    def getName(self):
        return "水果的名字是{}".format(self.__name)
    def getTaste(self):
        return "水果的味道是{}的".format(self._taste)


if __name__ == '__main__':
    f=_Fruit("苹果","甜")
    print(f.chandi)


