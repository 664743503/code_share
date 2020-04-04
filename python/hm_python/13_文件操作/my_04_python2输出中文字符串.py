# coding=utf-8

# 引号前面的u表示这是一个utf-8编码格式的字符串
# 如果去掉这个u，则不会显示这个世界，而是显示6个乱码
hello_str = u"hello世界"

print(hello_str)

for c in hello_str:
    print(c)
