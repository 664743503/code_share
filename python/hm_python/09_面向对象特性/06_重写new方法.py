class MusicPlayer(object):
    """
    重写new方法是固定的：
    1.一定要return super().__new__(cls)，
        如果不return，则python解释器得不到空间的对象引用，
        就不会调用object的初始化方法
        类似于c中的malloc一样
    2.new方法是一个静态方法，调用时，必须要传递cls参数
    """
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls)

    def __init__(self):
        print("init MusicPlayer")


player = MusicPlayer()
print(player)
