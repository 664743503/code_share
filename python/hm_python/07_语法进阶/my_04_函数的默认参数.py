gl_list = [4, 6, 2, 8]


gl_list.sort()

print(gl_list)


# 默认参数要放到最后定义
def print_info(name, title="", gender=True):

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s" %(title, name, gender_text))


print_info("小明", "班长")
print_info("小红", gender=False)
