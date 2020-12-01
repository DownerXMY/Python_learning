# 定义一个学生Student类。有下面的类属性：
# 姓名 name
# 年龄 age
# 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 获取学生的姓名：get_name() 返回类型:str
# 获取学生的年龄：get_age() 返回类型:int
# 返回3门科目中最高的分数。get_course() 返回类型:int
# zm = Student('zhangming',20,[69,88,100])

class Student:
    name1 = []
    age1 = []
    score1 = []
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self. score = score
        Student.name1.append(self.name)
        Student.age1.append(self.age)
        Student.score1.append(self.score)
    @classmethod
    def get_name(cls):
        print(Student.name1)
    @classmethod
    def get_age(cls):
        print(Student.age1)
    @classmethod
    def get_maxscore(cls):
        for j in range(1,3,1):
            max = 0
            for i in range(1,4,1):
                t = Student.score1[j-1]
                if t[i-1] > max:
                    max = t[i-1]
            Student.score1[j-1] = max
        print(Student.score1)

zm = Student(name = 'Zhangming', age = 20, score = [69, 88, 100])
gf = Student(name = 'Gaofeng', age = 22, score = [95, 84, 87])
Student.get_name()
Student.get_age()
Student.get_maxscore()

# 当然我们可以去尝试函数调用能不能行

class Student:
    name1 = []
    age1 = []
    score1 = []
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self. score = score
        Student.name1.append(self.name)
        Student.age1.append(self.age)
        Student.score1.append(self.score)
    @classmethod
    def get_name(cls):
        print(Student.name1)
    @classmethod
    def get_age(cls):
        print(Student.age1)
    @staticmethod
    def my_max(A):
        max1 = 0
        for k in range(1,len(A)+1,1):
            if A[k-1] > max1:
                max1 = A[k-1]
        return max1
    @classmethod
    def get_maxscore(cls):
        for j in range(1,3,1):
            Student.score1[j-1] = Student.my_max(Student.score1[j-1])
        print(Student.score1)

zm = Student(name = 'Zhangming', age = 20, score = [69, 88, 100])
gf = Student(name = 'Gaofeng', age = 22, score = [95, 84, 87])
Student.get_name()
Student.get_age()
Student.get_maxscore()

# 尝试一下函数调用函数的方法！
class Student:
    name1 = []
    age1 = []
    score2 = []
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self. score = score
        Student.name1.append(self.name)
        Student.age1.append(self.age)
        Student.score2.append(self.score)
    @classmethod
    def get_name(cls):
        print(Student.name1)
    @classmethod
    def get_age(cls):
        print(Student.age1)
    @staticmethod
    def my_max(A):
        max1 = 0
        for k in range(1,len(A)+1,1):
            if A[k-1] > max1:
                max1 = A[k-1]
        return max1
    @classmethod
    def get_maxscore(cls, **k):
        return Student.my_max(**k)

SQD = Student(name = 'SuQidong', age = 21, score = [100, 99, 98])
XMY = Student(name = 'XuMingyue', age = 22, score = [59, 56, 58])
Student.get_name()
Student.get_age()
# print(Student.score2)
# for j in range(1,3,1):
for j in range(1,3,1):
    T = Student.score2[j-1]
    print(Student.get_maxscore(A = T))

