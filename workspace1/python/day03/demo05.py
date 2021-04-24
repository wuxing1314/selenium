'''函数式编程'''

'''
高阶函数

如果一个函数(a)接收另外一个函数(b)作为参数，那么这个函数(a)就称为高阶函数

函数名就是一个指向函数的变量
当函数名后面跟一对()的时候表示调用函数
当函数名后面没有括号时，表示函数本身
'''

# 调用函数
print(abs(-10))

# 函数本身
print(abs) # <built-in function abs>

f = abs
print(f)
print(f(-5))

# abs = 9
# print(abs)
# print(abs(-5))


'''函数作为参数'''

def add(x,y):
    return x + y

print(add(2,3))
print(add(2,-3))

# 高阶函数
def add1(x,y,f):
    return f(x) + f(y)

print(add1(2,3,abs))
print(add1(2,-3,abs))

def power(x):
    return x*x

print(add1(2,-3,power))

# map()高阶函数
# y = f(x)  x = [0,1]
r = map(power,[1,2,3,4,5,6,7])
print(r)
print(list(r))

s = [power(i) for i in [1,2,3,4,5,6,7]]
print(s)

# reduce()高阶函数 - 要求传入的函数必须有2个参数
from functools import reduce

r = reduce(add,[1,2,3,4,5,6,7])
'''
add(1,2) 3
add(3,3) 6
add(6,4)

'''
print(r)


'''函数作为返回值'''

def s(*args): # arguments
    x = 0
    for i in args:
        x += i
    return x

print(s(13,7,5))
print(s(13,7,5,1,9,3))

'''
当lazy_s返回函数f时，相关的参数和变量都保存在返回的函数f中
我们把这种结构称为——闭包(Closure).

lazy_s函数每调用一次，都会返回一个新函数，即使参数相同
'''
def lazy_s(*args):
    def f():
        x = 0
        for i in args:
            x += i
        return x
    return f  # 函数最为返回值

a = lazy_s(13,7,5) # a是一个函数
b = lazy_s(13,7,5) # a是一个函数
print(a())
print(b())


'''匿名函数'''

print(list(map(power,[1,2,3,4,5,6])))

def f(i):
    return i*i
g = lambda i:i*i
print(g(3))

# lambda 表达式- 匿名函数
print(list(map(lambda i:i*i,[1,2,3,4,5,6])))
