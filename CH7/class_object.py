# 从这里开始要注意method和function之间的区别。
# 其实很简单，就是只有在class里面定义的function称为method
# class里面一个非常重要的method就是init，如下：

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def SayHello(self):
        print(f'Hello! My name is {self.name}, I am {self.age} years old.')
# 上例中，name和age称为attribute，init和SayHello都称为methods
# 当然绝大多数时候，我们还需要做class的实例化：
Mingyue_Xu = People(name = 'Mingyue Xu', age = 22)
Mingyue_Xu.SayHello()
# 这表示Mingyue_Xu是属于类People里的一个object，并且给定了属性name和age
# 注意method的调用方法是object.method()

