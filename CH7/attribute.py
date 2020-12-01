class Student:
    count = 0
    def __init__(self, name, gender, province):
        self.name = name
        self.gender = gender
        self.__province = province
    @property
    def province(self):
        return self.__province
    @province.setter
    def province(self, province):
        self.__province = province
Mingyue_Xu = Student(name = 'Mingyue Xu', gender = 'Male', province = 'Shanghai')

# 现在我们强调，name,gender这些当然是属性，是类中对象都有的属性；但是count也是属性，是整个类的属性。
print(Student.count)
# 但是Student.name是不行的，因为不是类属性，而是实例属性或者对象属性。
# 现在我们知道了Mingyue_Xu是类Student里的一个对象，那么虽然count是类属性，但是同样也是对象属性，比如我们可以打印：
print(Mingyue_Xu.count)
# 而且类属性不会被对象赋值所改变
Mingyue_Xu.count = 1
print(Mingyue_Xu.count)
print(Student.count)
# 同样很好理解的是，如果类属性被赋值改变，那么之后实例的对象属性也会跟着改变，比如下面新定义的Haoyu_Shi
# 但是如果说之前已经赋值的对象，就不会被改变，比如我们这里的Mingyue_Xu
Student.count = 2
print(Student.count)
print(Mingyue_Xu.count)
Haoyu_Shi = Student(name = 'Haoyu_Shi', gender = 'Male', province = 'Zhejiang')
print(Haoyu_Shi.count)
# 接下去我们要看看类属性的改变，比如说：
# 想要达到每做一次实例化，count都增加1的效果：
class Animal:
    count = 0
    def __init__(self, name):
        Animal.count = Animal.count + 1
        self.name = name
snake = Animal(name = 'snake')
bird = Animal(name = 'bird')
print(bird.count)
print(Animal.count)
dog = Animal(name = 'dog')
cat = Animal(name = 'cat')
print(snake.count)
print(bird.count)
print(dog.count)
print(cat.count)
print(Animal.count)
# 所以可以想象，这种方法可以统计类中总共有多少个对象。

