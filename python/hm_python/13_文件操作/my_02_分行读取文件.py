#!/usr/bin/python3 python3
# coding=utf-8

file = open("file.txt")

while True:
    text = file.readline()
    if not text:
        break
    # 此处不可以用 is None，会死循环
    # if text is None:
    #     break
    print(text)


file.close()
