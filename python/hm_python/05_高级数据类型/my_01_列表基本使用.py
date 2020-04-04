name_list = ["zhangsan", "lisi", "wangwu"]

# 1.查
# 输出下标为2的字符串
print(name_list[2])

# 知道内容，找下标
print(name_list.index("lisi"))

# 2.增
# append insert 和 extend
name_list.append("zhouyuan")
print(name_list)
name_list.insert(1, "wangxiaoer")
print(name_list)
temp_list = ["lindong", "xiaoyan"]
name_list.extend(temp_list)
print(name_list)

# 3.删
# remove pop del 和 clear
name_list.remove("lisi")
name_list.pop()
name_list.pop(1)
# del 是删除内存中的元素，如果是del name_list，则 name_list 整个内存空间都删除了
del name_list[0]
# del name_list
# name_list.clear()
# 注意：不能删除没有的元素
# name_list.remove("lisi")
print(name_list)

# 4.改
name_list[2] = "wo"
print(name_list)
