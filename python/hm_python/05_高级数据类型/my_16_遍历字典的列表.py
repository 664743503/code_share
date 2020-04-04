#!/usr/bin/env python
# coding=utf-8

students = [
    {"name":"小美"},
    {"name":"阿土"}
]

find_name = "张三"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了" + find_name)
        break

# 遍历完成之后，且没有执行break，才会走else
else:
    print("没找到" + find_name)

print("循环结束")
