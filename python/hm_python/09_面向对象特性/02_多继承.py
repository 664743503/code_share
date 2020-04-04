"""
1.如果一个类没有父类，则添加父类object让其继承
目的是为了python2和python3的兼容，python3默认的基类为object
而python2如果没有指定父类，则不会默认以object类为基类
"""
class A(object):
    def test(self):
        print("A test...")

    def demo(self):
        print("A demo...")


class B(object):
    def test(self):
        print("B test...")

    def demo(self):
        print("B demo...")


class C(B, A):
    pass



c = C()
c.test()
c.demo()
print(C.__mro__)
