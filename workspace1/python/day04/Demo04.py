'''访问限制'''


class Person:

    def __init__(self,name,age,gender):
        # 私有化成员变量，在变量前添加__
        self.__name = name #_Person__name
        self.__age = age  #_Person__age
        # 变量前添加一个_,也是私有化，也不应该直接访问
        self._gender = gender
        # __xxx__不是私有化变量，是系统特殊变量，可以直接访问

    # 添加getter/setter来访问私有化属性
    # 把属性封装起来，然后通过getter/setter方法来访问
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age>=0 and age <=120:
            self.__age = age
        else:
            raise NameError('年龄输入有误！')




julia = Person('Julia',18,'F')
# print(julia._Person__age)
# julia._Person__age = 17
# print(julia._Person__age)

# print(julia.__name) # 私有化的变量不允许直接访问
print(julia.get_name()) # 可以通过getter方法访问私有化的属性
julia.set_name('Julia Roberts')
print(julia.get_name())
julia.set_age(18)
print(julia.get_age())

julia.__age = 28  # 相当于给julia添加一个新的属性 __age
print(julia.__age)

print(julia._gender)