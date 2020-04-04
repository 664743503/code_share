class Tool(object):

    count = 0

    # 定义类方法：添加@classmethod
    @classmethod
    def show_tool_count(cls):
        print("tool count = %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 定义静态方法：添加@staticmethod
    @staticmethod
    def kill_something():
        print("kill something...")



tool1 = Tool("futou")
"""调用类方法"""
Tool.show_tool_count()
"""调用静态方法，不需要创建对象"""
Tool.kill_something()
