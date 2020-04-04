def measure():
    
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量开始...")
    # return (temp, wetness)
    # 如果函数返回的类型是元组，小括号可以省略
    return temp, wetness


result = measure()
print(result)

gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)

    
