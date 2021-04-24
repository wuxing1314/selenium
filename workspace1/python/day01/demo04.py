'''变量'''


# 在Python中，变量是没有类型的，但是数据是有类型的
# Python是动态语言
# = 是赋值符号
name = 'tom'
name = 'mike'
print(name)

a = 1
a = a + 1
print(a)

answer = True
answer = 'hello'

'''
变量的命名：
变量名必须是英文字母（大小写都可以），数字，和 _ 的组合
并且不能以数字开头

变量一般不要以大写开头
'''
t007 = 1
# 007t = 2 # 变量不能以数字开头

# _ 第一个作用，用于分隔单词
my_current_name = 'tony'
# _ 第二个作用，表示私有化
_name = 'tom'
__name = 'tom'


'''
常量
原则上不允许改变的量
常量要求所有字母大写
'''

PI = 3.1415926