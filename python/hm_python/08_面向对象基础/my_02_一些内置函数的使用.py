class Cat:

    def __init__(self, new_name):
        self.name = new_name

    def eat(self):
        print("%s 吃鱼" % self.name)

    def drink(self):
        print("%s 喝水" % self.name)

    def __del__(self):
        print("%s 挂了" % self.name)

    def __str__(self):
        # 必须要返回一个字符串
        return "我是小猫 %s" % self.name


tom = Cat("tom")
tom.eat()       #调用Cat类中的eat方法
tom.drink()     #调用Cat类中的drink方法
print(tom)      #调用Cat类中的__str__方法

#del tom # 可以主动销毁
print("-" * 50)
# 最后自动销毁对象tom
