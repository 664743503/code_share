i = 0
sum1 = 0
sum2 = 0

while i <= 100:
    if i % 2 == 0:
        sum1 += i
    if i % 2 == 1:
        sum2 += i
    i += 1

print("偶数之和sum = %d" % sum1)
print("奇数之和sum = %d" % sum2)