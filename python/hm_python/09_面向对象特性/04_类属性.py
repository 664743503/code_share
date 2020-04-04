class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具的数量
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")
print(Tool.count)
tool2 = Tool("刀子")
print(Tool.count)
tool3 = Tool("锯子")
print(Tool.count)
