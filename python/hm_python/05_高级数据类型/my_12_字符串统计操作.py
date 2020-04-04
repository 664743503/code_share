#!/usr/bin/env python
# coding=utf-8
hello_str = "hello hello"

# 1.统计字符串长度
print(len(hello_str))

# 2.统计某一个子字符串出现的次数
print("llo出现的次数为%d" % hello_str.count("llo"))

# 3.某一个子字符串出现的位置
print("llo第一次出现的下标为%d" % hello_str.index("llo"))

