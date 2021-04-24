'''实例属性和类属性'''


class Student:

    # 类属性- 不属于那一个具体的实例，属于类本身
    clazz = '39班'
    # 类属性最好不要与实例属性同名
    name = 'Jingying'

    def __init__(self,name):
        # 属性 - 实例属性
        self.name = name

tom = Student('Tom')
print(tom.name)
print(tom.clazz)

mike = Student('Mike')
print(mike.name)
print(mike.clazz)

print(Student.clazz)
print(Student.name)

