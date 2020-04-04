num = 10


def demo1():
    global num
    num = 99 #此时，修改了全局变量num的地址
    print("demo1 num = %d" % num)
    print("2---id(num) = %s" % id(num))


def demo2():
    print("demo2 num = %d" % num)
    print("3---id(num) = %s" % id(num))


print("1---id(num) = %s" % id(num))
demo1()
demo2()
