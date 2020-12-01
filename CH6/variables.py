x = 1
x += 1
print(x)

def demo():
    x = 10
    print(x)

demo()
print(x)
# 实际上是一个变量作用域的问题
# 函数体里面的参数，只在函数体里面有效

# 那么问题就来了，我们能不能在函数里修改定义在外面的全局变量呢？

def demo1(a):
    a = a + 10
    print(a)

demo1(a = x)
print(x)

y = [1, 2, 3]
def demo2(a):
    a.append(4)
    print(a)

demo2(a = y)
print(y)
# 注意以上的原因是什么呢？
# a = a + 10并没有对原先的a作出任何改变，但是append确实是对原先的a作出了改变。

z = [1, 2, 3]
def demo3(b):
    b = b + [4, 5, 6]
    print(b)

demo3(b = z)
print(z)

# 现在我们来讲怎么在函数体里修改外面的全局变量
w = 1
def demo4(c):
    global w
    w = w + c
    print(w)
# 注意如果没有global w这句话，python会报错！
demo4(c = 2)
print(w)
