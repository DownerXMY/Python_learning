# 装饰器这个东西我们已经接触很多次了，但是从来没有从本质上来介绍过装饰器
class Student:
    name1 = []
    gender1 = []
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        Student.name1.append(self.name)
        Student.gender1.append(self.__gender)
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender):
        self.__gender = gender
    @classmethod
    def Sayhello(cls):
        print('Hello world!')
    @classmethod
    def get_name(cls):
        return Student.name1
    @staticmethod
    def male_account():
        n = 0
        for item in Student.gender1:
            if item == 'Male':
                n += 1
        return n
Mingyue_Xu = Student(name = 'Mingyue_Xu', gender = 'Male')
Qidong_Su = Student(name = 'Qidong_Su', gender = 'Male')
Qianru_Yu = Student(name = 'Qianru_Yu', gender = 'Female')
print(f'My name is {Mingyue_Xu.name}, I am a {Mingyue_Xu.gender}')
print(Student.get_name())
print(Student.male_account())

# 以上包含了我们目前为止所学的所有装饰器。
# 当然，装饰器绝对不仅仅只在类中，还有很多重要的应用。

def test1(x):
    print(test1.__name__)
    return x * 2
def test2(x):
    print(test2.__name__)
    return x * x
# 当然这样写的话，在运行时就会打印出函数的名字：
test1(3)
test2(3)
# 不过我们的问题是，如果函数只是这样的：
def test3(x):
    return x * 2 + x
# 那么在不修改函数本身的前提下，怎么样打印出函数的名字呢？

# 这实际上会用到我们之前说的高阶函数的方法。
def demo1(f):
    def f_new(x):
        print(f.__name__)
        return f(x)
    return f_new
g = demo1(test3)
print(g(3))
g(3)

def demo2(f):
    return lambda x: (print(f.__name__), f(x))
h = demo2(test3)
print(h(3))
h(3)
# lambda表达式想要返回多个值，需要加括号！
# 注意，如果函数比较复杂，还是不建议使用lambda表达式。
# 最后，我们来看最方便的办法，就是装饰器：

@demo1
def test4(x):
    return x * 3 + x
print(test4(3))
# 看起来也并不简单，不过我们只是要说明，所谓装饰器，就是说把一个函数作为装饰器，然后在装饰器下新定义的函数将会附带装饰器里面函数的内容
# 比如这里的test4，就附带了demo1中的print的属性。

@demo2
def test5(x):
    return x * 2 + 1
print(test5(2))
# 回到之前的问题，看上去装饰器好像也是蛮麻烦的，那么究竟有什么好用之处呢？
# 什么是带参数的装饰器？
# 有一个参数个数的问题，比如我们来写一个高阶函数作为装饰器：

# def demo3(f):
#     return lambda x: print('只打印函数名字:', f.__name__)
# # 那么很显然这里输出的函数只允许传入一个参数
# @demo3
# def test6(x, y):
#     return x + y
# test6(1, 3)

# 可以运行看看，这时候是会报错的，因为在test6中我们传入了2个参数
# 想要解决这个问题，就要用到(可变)参数的装饰器：
def demo4(f):
    return lambda *args, **kwargs: (print('只打印函数的名字:', f.__name__), f(*args, **kwargs))

@demo4
def test7(x1, x2, x3, x4):
    return x1 + x3 + x4

print(test7(1, 4, 2, 7))
# 这实际上就是说，如果我们在写装饰器的时候，写成可变参数，那么后面用装饰器的时候就不用去纠结参数个数的问题了。

# 那么还有的时候，我们希望装饰器本身也能够带一个参数：
def demo5_new(a):
    def demo5(f):
        return lambda *args, **kwargs: (print('函数的名字是:', f.__name__), a * f(*args, **kwargs))
    return demo5

e = int(input('请输入一个数字'))
@demo5_new(a = e)
def test8(x, y, z):
    return x * y + z

print(test8(1, 4, 2))
# 换句话说，就是新的装饰器demo5_new实际上也是一个高阶函数，输入是参数a，输出的还是一个高阶函数demo5
# 那比如说，我们想着能不能全部写成lambda表达式：
# def demo6_new(a):
#     return lambda f, *args, **kwargs: (print('打印函数的名字:', f.__name__), a * f(*args, **kwargs))
#
# @demo6_new(a = 3)
# def test9(x, y, z):
#     return x + y * z
#
# print(test9(x = 1, y = 4, z = 2))
# 这段代码是报错的，不难理解。

# 到这里，我们大概有点明白了，学习高阶函数，其实有一部分是为了学习装饰器服务的。

# 最后，装饰器还有一块内容需要完善：
def demo_r(f):
    return lambda *args, **kwargs: (f.__name__, f(*args, **kwargs))
@demo_r
def test_r(x, y, z):
    '''
    this is test_r!
    x, y, z :parameters!
    '''
    return x + y * 3 - z
print(test_r(1, 4, 2))

# test_r被装饰过以后，本身的属性会有一些变化：
print(test_r.__name__)
print(test_r.__doc__)  # 打印test_r的注释
# 解释起来也很简单，就是说当我们加上装饰器的时候，test_r获取到的名字实际上是函数的lambda表达式
# 又或者，如果我们把装饰器写成这样：

import functools

def demo_r1(f):
    @functools.wraps(f)
    def f1(*args, **kwargs):
        print('函数的名字是:', f.__name__)
        return f(*args, **kwargs)
    return f1
@demo_r1
def test10(x, y, z):
    '''
    this is test10!
    :param x:
    :param y:
    :param z:
    :return:
    '''
    return x + y * 3 - z

print(test10(1, 4 ,2))
print(test10.__name__)
print(test10.__doc__)
# 这时候其实test10获取到的名字是装饰器里的f1
# 那么实际上Python为我们提供了一种快速把test10的属性复制到f1的方法，需要我们引入内置模块functools,然后加一个装饰器functools.wraps
# 这样以后再试一下，就会发现属性已经恢复了。
# 这件事情实际上一般是默认都要做的，可以成为一种习惯。

