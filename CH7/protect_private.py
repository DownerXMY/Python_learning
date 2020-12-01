class People:
    def __init__(self, name, school, age):
        self._name = name
        self.__school = school
        self.age = age

    def SayHello(self):
        print(f'Hello! My name is {self._name}, I am from {self.__school} and I am {self.age} years old.')
    def get_change_school(self):
        print(Mingyue_Xu.__school)
        Mingyue_Xu.__school = 'PKU'
        print(Mingyue_Xu.__school)


Mingyue_Xu = People(name = 'Mingyue Xu', school = 'SJTU', age = 22)
Mingyue_Xu.SayHello()

# 我们要说的是私有属性和受保护属性。
# 注意，我们不仅可以直接访问object的age这个属性，还可以直接改变它的值，那么显然age是不受保护的。
print(Mingyue_Xu.age)
Mingyue_Xu.age = 30
print(Mingyue_Xu.age)
# 那么怎么样变成受保护的属性呢，我们以name为例，实际上就是加一个下划线这么简单。
print(Mingyue_Xu._name)
Mingyue_Xu._name = 'Downer'
print(Mingyue_Xu._name)
# 依旧可以访问，也还是可以改变，那么怎么样才能拒绝访问和改变呢？实际上就是要加双下划线，以下程序会报错！
# print(Mingyue_Xu.__school)
# Mingyue_Xu.__school = 'PKU'
# print(Mingyue_Xu.__school)

# 但实际上，private属性能且仅能在class里面访问和更改。
Mingyue_Xu.get_change_school()
print(dir(Mingyue_Xu))
# 以上目录中我们能看到所有可以访问的对象，没有__school，这就很容易理解为什么私有属性不能在class外访问了。
# 但是令人惊奇的是，居然有一个叫_People__school的东西，说明我们实际上还是可以访问，具体这么做：
print(Mingyue_Xu._People__school)
# 而且甚至还能够修改：
Mingyue_Xu._People__school = 'TKU'
print(Mingyue_Xu._People__school)
# 最后，虽然依旧可以访问，但是非常不建议这么做！


