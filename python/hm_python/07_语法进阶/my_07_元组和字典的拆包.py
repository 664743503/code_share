def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1,2,3)
gl_dict = {"name":"xiaoming", "ags":18}

# 在元组变量前，加一个*，传递给args
# 在字典变量前，加两个*，传递给kwargs
demo(*gl_nums, **gl_dict)
