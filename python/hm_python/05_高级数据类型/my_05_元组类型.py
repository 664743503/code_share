#!/usr/bin/env python
# coding=utf-8

# 1.元组不能增删元素

# 2.空元组
info_tuple = ()


info_tuple = ("zhangsan", 18, 175)
print("info_tuple = ", end="")
print(info_tuple)

# 3.只包含一个元素时,不能这么写
single_tuple = (50)
print(type(single_tuple))

# 4.这么写才是只包含一个元素
single_tuple = (50, )
print(type(single_tuple))

# 5.取值和取索引
print("info_tuple的下标为0的元素是%s" % info_tuple[0])
print("info_tuple的下标为2的元素是%d" % info_tuple[2])
print("info_tuple元素为18的下标为%d" % info_tuple.index(18))
print("info_tuple元素为zhangsan的下标为%d" % info_tuple.index("zhangsan"))

# 6.统计个数
print("info_tuple的元素zhangsan总个数为%d" % info_tuple.count("zhangsan"))
