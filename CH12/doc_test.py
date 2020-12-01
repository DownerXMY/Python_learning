# 程序编写与修正中很重要的两块内容是，调试(已经讲了)和测试。
# 文档测试
# 比如我们有一个很简单的函数demo如下：

def demo(x, y):
    '''这是注释！'''
    return x + y

print(demo.__name__)
print(demo.__doc__)

# 那么什么叫做文档测试呢，实际上就是把在终端的运行结果加到我们这里代码的注释里，比如说这样：

def demo(x, y):
    '''
    >>> demo(1,2)
    3
    >>> demo('1','2')
    '12'
    >>> demo([1,2],[3,4])
    [1, 2, 3, 4]
    >>> demo(1,'2')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>
    '''
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# 那么比如我们如果把3改成4，那么就会提示我们测试里面会有一个测试出错。
def demo(x, y):
    '''
    >>> demo(1,2)
    4
    >>> demo('1','2')
    '12'
    >>> demo([1,2],[3,4])
    [1, 2, 3, 4]
    >>> demo(1,'2')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>
    '''
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod()


