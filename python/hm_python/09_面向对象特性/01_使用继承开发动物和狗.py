class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")


xtq = XiaoTianQuan()
xtq.eat()
xtq.drink()
xtq.bark()
xtq.fly()
