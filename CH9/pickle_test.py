import pickle

class Student:
    school1 = []
    def __init__(self, name, gender, school):
        self.name = name
        self.__gender = gender
        self.school = school
        Student.school1.append(self.school)
    @property
    def gender(self):
        return self.__gender
    def SayHello(self):
        print('Hello!')
    @classmethod
    def get_school(cls):
        return Student.school1
f = open('Mingyue_Xu', mode = 'rb')
Mingyue_Xu1 = pickle.load(f)
f.close()
print(Mingyue_Xu1)
print(Mingyue_Xu1.name, Mingyue_Xu1.gender, Mingyue_Xu1.school)
Mingyue_Xu1.SayHello()

# 注意，类Student还是不能省略，因为这相当于是基础定义。
# 可以看到这时候就加载成功了。
# 注意，如果想要加载私有属性，那么装饰器在加载方同样是需要写出来的;或者不加装饰器，但是需要Mingyue_Xu1._Student__gender


