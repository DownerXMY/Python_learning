import pickle

class Student:
    school1 = []
    def __init__(self, name, gender, school):
        self.name = name
        self.__gender = gender
        self.school =school
        Student.school1.append(self.school)
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender):
        self.__gender = gender
    def SayHello(self):
        print('Hello!')
    @classmethod
    def get_school(cls):
        return Student.school1
Mingyue_xu = Student(name = 'Mingyue_Xu', gender = 'Male', school = 'SJTU')
Haoqi_Yuan = Student(name = 'Haoqi_Yuan', gender = 'Male', school = 'PKU')
print(Student.get_school())

# 这次我们来说说序列化Python对象
# 我们现在有一个需求，就是把这里的Mingyue_Xu和Haoqi_Yuan传给别人，另外一个使用Python的人，是的他在他的电脑中能够加载出来。
# 并且可以访问对象的属性和方法。
# 那么这时候就需要用到内置的库pickle了。

f = open('Mingyue_Xu', mode = 'wb')
# 注意往文件里写入Python的对象必须采用二进制，所以这里是'wb'
pickle.dump(Mingyue_xu, f)
f.close()
# 到这里运行代码，这时候会发现能够生成一个叫做Mingyue_Xu的二进制文件。
# 不过这个新的文件是打不开的，但是可以加载出来，将在pickle_test.py中演示。

