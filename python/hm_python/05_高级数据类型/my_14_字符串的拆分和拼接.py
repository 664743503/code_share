#!/usr/bin/env python
# coding=utf-8

poem_str = "登鹳雀楼 \t 王之涣 \t 白日依山尽\t \n 黄河入海流 \t\n 欲穷千里目 \t\t 更上一层楼 \n"

print(poem_str)
print("----------------------------------------")

poem_list = poem_str.split()
print(poem_list)
print("----------------------------------------")

poem_result = "\n".join(poem_list)
print(poem_result)

num_str = "0123456789"

# 第一个值表示开始，第二个值表示结束的位置，第三个值表示步长。
# 第一个值为-1表示倒数最后一个值，-2表示倒数第二个值。是正值，则表示下标位置。为空表示默认为0
# 第二个值同上，但是为空默认表示为最后一个值
# 第三个值一般不填，默认为1，表示每次往后移一位。填2表示每次往后移两位。
print(num_str[1::2])

print(num_str[::-1])
# 或者如下
print(num_str[-1::-1])
