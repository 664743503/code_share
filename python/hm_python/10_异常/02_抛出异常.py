def input_password():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    exc = Exception("密码长度不够")
    raise exc
    

try:
    print(input_password())
except Exception as result:
    print(result)
