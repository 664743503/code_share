# 1.输出5行星星
i = 0
while i <= 5:
    print("*" * i)
    i += 1

# 2.技巧
# 说明:此处的end=表示最后不是换行,而是一个空字符
print("*", end="")
print()     # 此处输出空,表示换行
print("*", end="--")
print("*")
print("---------------------")

# 3.双层循环输出星星
i = 0
while i <= 5:
    # print("*")
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print("")
    i += 1
