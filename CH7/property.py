class People:
    def __init__(self, name, age, school, birth, girl):
        self.name = name
        self.age = age
        self.school = school
        self._birth = birth
        self.__girl = girl
    @property
    def girl(self):
        return self.__girl
    @girl.setter
    def girl(self, girl):
        if girl == 'dog':
            print('FUCK')
        else:
            self.__girl = girl.upper()
    def Say_Hello(self):
        print(f'我的名字是{self.name}，生于{self._birth}，今年{self.age}岁了，来自{self.school}，不告诉你{self.__girl}是不是我的女朋友。')

Mingyue_Xu = People(name = 'Mingyue Xu', age = 22, school = 'SJTU', birth = '1998-12-14', girl = 'Brie')
Mingyue_Xu.Say_Hello()

# 实际上除了之前的方法，还有别的访问私有属性的简便方法。
# 这就是要在class里设置一个装饰器，即@property。
print(Mingyue_Xu.girl)
# 同样，还可以用装饰器的方式改变私有属性的值。
Mingyue_Xu.girl = 'dog'
print(Mingyue_Xu.girl)
# 注意print的基础是装饰器，换句话说，不能写成print(Mingyue_Xu.__girl)，这是错的！
# 那么不禁想问，这和之前的访问修改方法，也就是Mingyue_Xu._People__girl有什么区别呢？
# 当然是有的，因为我们可以吧修饰器下的method变得复杂，加一下限制，比如说，把名字全部变成大写(.upper())；再比如，名字不能取成恶意的(FUCK)。

