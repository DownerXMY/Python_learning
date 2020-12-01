# 什么是异常？
# 比如我们现在来看一个很简单的例子--列表解析

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [i for i in a if 11 % i == 0]
# print(b)
# print('Finished')

# 惊奇地发现会有一个被0除的错误
# 一旦发生错误，程序就会中断，所以最后的Finished也是没有打印出来。
# 异常分为两种，一种是内置的异常，比如我们这里遇到的ZeroDivisionError, IndexError, AttributeError, 等等
# 另外一种是我们自定义的异常，后面会讲到。

# 那么如何捕捉和处理异常呢？
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    b = [i for i in a if 11 % i == 0]
except:
    print('异常')
print('Finished')
# 这样程序就不会中断了。
# 实际上还能更加精确地捕捉错误，如下：
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    b = [i for i in a if 11 % i == 0]
except ZeroDivisionError:
    print('异常')
print('Finished')

# 但是这么做也有一个问题，比如程序中可能有别的错误，比如说：

# a = ['str', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# try:
#     b = [i for i in a if 11 % i == 0]
# except ZeroDivisionError:
#     print('异常')
# print('Finished')
# 程序还是会报错, TypeError!

# 再或者，麻烦点，可以这样：
a = ['str', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    b = [i for i in a if 11 % i == 0]
except ZeroDivisionError:
    print('异常1')
except TypeError:
    print('异常2')
print('Finished')

# 然后我们来说一下如何自定义一个异常：
class MyError(Exception):
    pass

try:
    raise MyError('这是自定义的异常')
except MyError as e:
    print(e)



