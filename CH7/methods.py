class Student:
    count = 0
    def __init__(self, name, school, gender, city):
        Student.count = Student.count + 1
        self.name = name
        self.school = school
        self.gender = gender
        self.__city = city
    @property
    def city(self):
        n = 0
        while n < 3:
            n += 1
            a1 = int(input('请输入密码:'))
            if n < 3:
                if a1 == 123456:
                    return self.__city
                else:
                    print('输入错误,请重试!')
            else:
                print('输入次数过多!')
    @city.setter
    def city(self, city):
        self.__city = city
    def Say_Hello(self):
        print(f'Hello, My name is {self.name}, I am from {self.school} in {self.__city}.')
    @classmethod
    def describtion(cls):
        print('这里是学生列表')
        Student.test()
    @staticmethod
    def test():
        print('这是一个静态方法！')

Mingyue_Xu = Student(name = 'Mingyue_Xu', school = 'SJTU', gender = 'Male', city = 'Shanghai')
Haoyu_Shi = Student(name = 'Haoyu_Shi', school = 'ZJU', gender = 'Male', city = 'Hangzhou')
print(Mingyue_Xu.city)
Mingyue_Xu.Say_Hello()
Haoyu_Shi.Say_Hello()
# 注意我们一直没讲过这里的self，实际上很简单，他就代表了类中的一个实例或者一个对象。
# 那么和之前一样，既然有类属性和对象属性之分，自然也就会有类方法和对象方法之分。
# 比如这里的就是一个类方法，不带参数self，需要加装饰器！
Mingyue_Xu.describtion()
Haoyu_Shi.describtion()
Student.describtion()

# 接下去我们介绍第三种方法，之前讲了类方法，实例(对象)方法，下面还有一个静态方法：
# 比如这里的，注意加的装饰器不一样，可以不需要带参数！
Student.test()
Mingyue_Xu.test()
Haoyu_Shi.test()

# 那么区别在哪里呢？
# 在类方法中，可以调用别的方法，包括静态方法。
# 但是在静态方法中，不能调用类方法，因为它没有cls这个参数。

# 最后一个问题，类方法或者静态方法里面能不能调用对象方法？
# 比如在description或者test中调用Say_Hello可不可以？
# 答案是不行的，因为类方法或者静态方法中没有self的参数。

