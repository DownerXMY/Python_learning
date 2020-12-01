def add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise ValueError('输入错误！')

# 怎么写单元测试呢？
# 我们需要在文件unit_test.py所在的包外面新建一个测试文件，比如叫做test_1.py
# 就相当于模块调用的方式在测试文件里调用函数add

