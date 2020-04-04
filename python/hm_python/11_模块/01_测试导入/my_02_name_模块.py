#!/usr/bin/python3 python3
# coding=utf-8

"""
1.模块开发原则：每一个文件都是可以被导入的
2.一个独立的python文件就是一个模块
3.在导入文件时，文件中所有没有任何缩进的代码都会执行一遍！
4.实际开发中，当不想执行测试代码时，就要使用__name__属性
"""


"""导入自己什么都不会发生"""
import my_02_name_模块


def say_hello():
    """导入此模块，不会调用工具类代码，即不会调用非缩进行代码"""
    print("02 name 模块中 say_hello函数")
    

"""
1.__name__是python的一个内置属性，记录着一个字符串
2.如果是被其他文件导入的，__name__就是模块名
3.如果是当前执行的程序，__name__是__main__
4.所以很多python文件中都会有以下格式的代码
"""

def main():
    print(__name__)
    say_hello()


# 根据__name__判断是否执行下方代码
if __name__ == "__main__":
    main()

