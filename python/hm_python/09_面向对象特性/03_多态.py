class Dog(object):

    def __init__(self, name):
        self.name = name
        
    def game(self):
        print("%s play games..." % self.name) 


class XiaoTianQuan(Dog):

    def game(self):
        print("%s fly and play games..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s and %s are happy with the play..." % (self.name, dog.name))

        dog.game()


xiaohuang = Dog("小黄")
xiaoming = Person("小明")
feitiangou = XiaoTianQuan("飞天神犬")
"""
1.此处即是多态，Person类中只需要让狗调用game方法，而不关心具体是什么狗
2.在程序执行时，传入不同的狗对象实参，就会产生不同的执行结果
""" 
xiaoming.game_with_dog(xiaohuang)
print("-"*50)
xiaoming.game_with_dog(feitiangou)

