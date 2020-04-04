# 方法1：用*接收一个元组
def sum_numbers(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


gl_sum = sum_numbers(1,2,3,4,5,-1,-2,-1.22)
print(gl_sum)


# 方法2：不用*，直接传递元组参数
def sum_numbers2(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


gl_sum = sum_numbers2((1,2,3,4,5,-1,-2,-1.22))
print(gl_sum)

