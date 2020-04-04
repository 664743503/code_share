class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secert(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))
        

xiaofang = Women("xiaofang")
# print(xiaofang.__age) #不能直接在外界调用类的私有变量
print(xiaofang._Women__age)
xiaofang._Women__secert()

