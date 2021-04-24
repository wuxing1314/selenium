'''继承和多态'''

# 自定义类型
# 类名首字母要大写
class Animal(object): # object是所有类的父类
    # 系统默认会提供一个构造方法
    def __init__(self,name):
        self.name = name

    def run(self):
        print('动物%s正在奔跑...'%self.name)

class Dog(Animal): 
    '''
    让Dog类继承Animal类，
    Animal叫做父类，或超类，Dog叫做子类
    
    继承父类的属性和方法
    '''
    # pass

    # 子类除了继承父类的方法以外，还可以有自己独有的方法
    def eat(self):
         print('狗狗%s在啃骨头...'%self.name)

    def run(self):
        print('狗狗%s在奔跑...'%self.name)

class Cat(Animal):

    # 重写 - 子类重写了父类的方法
    def run(self):
        print('猫猫%s在爬树...'%self.name)

a = Animal('笨笨')
a.run()

dog = Dog('旺财')
dog.run()
dog.eat()

cat = Cat('来福')
cat.run()

# 某一个类的具体对象也称为 实例-instance
from collections.abc import Iterable

flag = isinstance([1,2,3],Iterable)
print(flag)

# isinstance()  判断某个对象是否是某个类的一个实例
# 判断某个对象是否是某个类型
flag = isinstance(cat,Dog)

# 多态 - dog对象既是Dog类型，又是Animal类型，我们把这种现象就称为多态
flag = isinstance(dog,Dog)
flag = isinstance(dog,Animal)
print(flag)
# 子类对象可以看做父类的实例，但是反过来不行
flag = isinstance(a,Animal)
flag = isinstance(a,Dog)

# 多态应用
def 跑2次(animal):
    animal.run()
    animal.run()

跑2次(a)
跑2次(dog)
跑2次(cat)
