class Cat:
    
    def eat(self):
        print("吃鱼")

    def drink(self):
        print("喝水")


tom = Cat()
tom.eat()
tom.drink()

print(tom)
print("%x" % id(tom))
