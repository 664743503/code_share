#!/usr/bin/python3 python3
# coding=utf-8

"""
1.打开
2.读
3.写
4.关闭
"""

"""
r:只读
w:只写，覆盖写
a:追加
r+:读写。文件指针在开头
w+:读写。覆盖写
a+:读写。文件指针在末尾
"""
file = open("file.txt", "a")
file.write("hello")
file.close()

file = open("file.txt", "r")
# 执行了一次read方法之后，文件指针移动到文件末尾，再次调用不会读取到任何内容
text = file.read()
print(text)
file.close()
