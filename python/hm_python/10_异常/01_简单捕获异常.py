try:
    num = int(input("请输入一个整数:"))
    num1 = 8 / num
    print(num1)
# except ZeroDivisionError:
#     print("除0错误")
except ValueError:
    print("异常：未输入正确的整数")
except Exception as result:
    print("异常：未知的错误 %s" % result)
else:
    print("未出现异常，会执行else")
finally:
    print("无论有没有异常，都会执行finally")
