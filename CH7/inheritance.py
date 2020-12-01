class People:
    def __init__(self, name, age, school, birth):
        self.name = name
        self.age = age
        self.__school = school
        self.__birth = birth
    @property
    def birth(self):
        return self.__birth
    @property
    def school(self):
        return self.__school
    # 为了让我们能够在外面访问私有属性
    @school.setter
    def school(self, school):
        self.__school = school
    # 时常牢记这里的school是一个属性，并非一个函数
    # 为了让我们能够在外面修改私有属性
    def change_school(self):
        self.__school = 'SJTU'
Mingyue_Xu = People(name = 'Mingyue Xu', age = 22, school = 'FDU', birth = '1998-12-14')
Mingyue_Xu.change_school()
print(f'我叫{Mingyue_Xu.name}，今年{Mingyue_Xu.age}岁了，来自{Mingyue_Xu.school}，生于{Mingyue_Xu.birth}.')

# 什么叫做继承和多态？
# 直观上，可以理解成子类继承父类的一些东西。
class Animal:
    def eat(self):
        print('Animal is eating!')
# 怎么定义Animal的一个子类呢？
class Bird(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} is eating!')
    def sleep(self):
        print(f'{self.name} is sleeping!')
# 那么子类会拥有一切父类中的methods，当然也可以有自己独有的methods，当然父类中的对象肯定不会有子类中的methods
Passer = Bird(name = 'Passer')
Passer.eat()
Passer.sleep()
Dog = Animal()
Dog.eat()
# 错误代码：Dog.sleep()
# 接下来的一个问题是，如果子类和父类中有同样名字的method，会怎么样？
# 可以看到，子类中的method运行的结果将覆盖父类中method运行的结果，这种现象就称为"多态"

# 最后让我们来看看"多态"的好处：
def demo(a):
    a.eat()

for a in [Passer, Dog]:
    a.eat()
# 这实际上表明，当子类和父类有相同的method时，如果调用，子类中的对象优先输出子类中作用的结果，而父类中的对象只能输出父类中作用的结果。
# 总之一句话，有子类方法优先子类；子类没有优先父类；连父类也没有，就报错！
