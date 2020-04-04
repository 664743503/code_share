# 参数前面有一个*，表示是元组参数
# 参数前面有两个*，表示是字典参数
def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(1000)

demo(1,         #第一个参数num
     2, 3, 4,   #第二个参数nums
     name="xiaoming", age=18, gender=True)  # 第三个参数person
