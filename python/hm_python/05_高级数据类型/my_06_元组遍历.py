#!/usr/bin/env python
# coding=utf-8

info_tuple = ("zhangsan", 18, 1.75)

print("%s的年龄为%d, 身高%.2f米" % info_tuple)

# 格式化字符串后面的%()本质上就是元组
print("%s的年龄为%d, 身高%.2f米" % ("小明", 20, 1.8))

# 元组可以如下所示，添加成新的字符串
info_str = "%s的年龄为%d, 身高%.2f米" % info_tuple
print(info_str)


for my_info in info_tuple:
    """
    使用格式字符串拼接 my_info 这个变量不方便！
    因为元组的元素类型一般是不同的！
    """
    print(my_info)


# P180
