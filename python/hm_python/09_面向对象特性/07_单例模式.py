class MusicPlayer(object):

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print("init MusicPlayer")
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
