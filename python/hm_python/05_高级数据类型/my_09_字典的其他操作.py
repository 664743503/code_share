#!/usr/bin/env python
# coding=utf-8

xiaoming_dict = {"name":"小明",
                 "age":18
                }

# 1.统计键值对数量
print(len(xiaoming_dict))

# 2.合并字典
temp_dict = {"height": 1.75,
             "age": 20
            }
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)

# 3.清空字典
temp_dict.clear()
print(temp_dict)

# 4.遍历字典
for k in xiaoming_dict:
    print("%s - %s" %(k, xiaoming_dict[k]))
