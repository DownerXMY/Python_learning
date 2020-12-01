# 学会了模块和包，就能开始接触复杂项目了。
def my_sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

# 想象一下，如果一个复杂程序很长，比如有几千行，那么实际上是很不利于我们去维护的。
# 这时候就需要把整个文件分成若干块，每一块就可以成为一个模块，模块可以是一个文件。
# 一般模块里会放一些通用的函数/方法/类/算法等等。比如说求最大值，求平均数什么的。
def my_max(*a):
    max = 0
    for j in a:
        if j > max:
            max = j
    return max

class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender):
        self.__gender = gender

# 很显然我们希望这个文件(模块)能够被其他的文件(模块)调用。
# 实际上，我们需要把模块放进一个package，然后调用package。

# 创建package很简单，创建完了以后，会自动生成一个初始文件__init__.py
# 然后我们可以把刚刚写的文件移入package中。
# 接下去我们会在test.py中演示如何调用package_demo

print('1 + 6 + 2 + 4 =', my_sum(1,6,2,4))
print(__name__)

if __name__ == '__main__':
    print('1 + 5 + 3 + 9 =', my_sum(1,5,3,9))

