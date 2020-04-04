"""import会先在当前目录查找导入的模块，然后才会到系统目录下查找"""
import random

rand = random.randint(0, 10)

print(rand)
