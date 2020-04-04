#!/usr/bin/python3 python3
# coding=utf-8

# 1.打开文件
file_read = open("file.txt")
file_write = open("file.txt.backup", "w")

# 2.写入大文件
# text = file_read.read()
# file_write.write(text)
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)


# 3.关闭文件
file_write.close()
file_read.close()
