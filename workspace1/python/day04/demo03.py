'''
面向对象编程
Object Oriented Programming OOP

'''
5 # int
'abc' # str
abs # function

# 数据
student1 = {'name':"Tom",'math':99,'python':88}
student2 = {'name':'张三丰','math':95,'python':90}

# 处理数据的函数
def print_score(student):
    print(student['name'],student['math'],student['python'])

print_score(student1)
print_score(student2)

# 创建Student类-把数据和处理数据的函数封装在一起
'''
面向对象的第一个特点：封装
把数据和处理数据的函数封装在一起
'''
class Student:

    # methon - 方法
    # 方法的第一个参数必须是self,并且是系统自动传参,
    # self指代的是当前对象
    # __init__()方法也称为——构造方法Constructor
    def __init__(self,name,math,python):
        # name 是局部变量-作用范围仅限于定义它的函数
        # self.name 是成员变量-作用范围在在定义它的类中
        # 成员变量也称为 属性
        self.name = name
        self.math = math
        self.python = python

    # 成员方法 - 行为
    def print_score(self):
        print(self.name,self.math,self.python)

# 创建Student类的一个实例对象 stu1
stu1 = Student('Tom',99,88) # 调用__init__()方法
stu2 = Student('张三丰',95,90)


print(stu1.name)
print(stu1.math)
print(stu1.python)

stu1.print_score()
stu2.print_score()

'''
类Class和实例Instance
类是一个抽象的模板
实例就是根据类创建出的一个一个具体的 对象
'''

# 创建Student类的一个实例
tom = Student('Tom',95,97)

# 调用对象的属性
print(tom.name)

# 可以自由的给实例绑定属性
tom.gender = '男'
print(tom.gender)

mike = Student('Mike',88,89)
print(mike.name)
mike.print_score()

print(tom)
print(mike)


'''访问限制'''

# 可以从类的外部直接访问类的属性
print(tom.math)
tom.math = -100
print(tom.math)