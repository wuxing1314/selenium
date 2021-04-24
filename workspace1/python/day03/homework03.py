# 0. 测试元组生成式和字典生成式

# 1. 实现一个trim()函数，利用切片去除字符串前后的空格
#    ' tom  '

# 递归方法
def trim(s):
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    return s

s = trim(' tom cruse ')
print(s)
print(len(s))

# 循环方式
def trim2(s):
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    return s

s = trim2(' tom cruse ')
print(s)
print(len(s))

# 2. 随机生成一个5位的验证码，包含A-Za-z0-9
import random
import string

def sample(S,n):
    r = ''
    for i in range(n):
        r = r+S[random.randint(0,len(S)-1)] # 运算符重载
    return r

S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
print(sample(S,5))
print(string.ascii_letters)
print(string.digits)


# 3. 将下面列表中的所有字符变为小写：(列表生成式)
#     ['Tom','MIKE','VM','Python']
#     'Tom'.lower()
l = ['Tom','MIKE','VM','Python']
m = [e.lower() for e in l]

# 4. 使用迭代查找一个列表中的最大值和最小值，返回一个tuple

def f(l):
    # 避免引入脏数据
    max = l[0]
    min = l[0]

    for i in l:
        if i > max:
            max = i
        elif i < min:
            min = i
    return min,max

l = [3,7,12,1,5,23]
print(f(l))

# 5. 利用map函数将字符串首字母变为大写
# ['tom','MIKE','Tony'] -> ['Tom','Mike','Tony']

names = ['tom','MIKE','Tony'] 
new_names = map(lambda y:y[0].upper()+y[1:].lower(),names)

def g(x):
    return x[0].upper()+x[1:].lower()

new_names = map(g,names)

print(list(new_names))


'''     选做题    '''
# 6. 使用生成器构造一个自然数序列 1，2，3，4，5.....



# for i in n:
#     print(i)
#     time.sleep(1)


# 7. 使用闭包实现 计数器函数

# 不安全
# count = 0
# count += 1

def counter():
    s = [0]
    def count():
        # 计数
        s[0] += 1
        # 返回当前计数结果
        return s[0]
    return count

count = counter()
print(count())
print(count())
print(count())
print(count())
print(count())
print(count())



# 内部函数引用了外部函数的变量，称为闭包

print('------------------------------')
# 8. 实现一个计时器装饰器
import time


def decorator(func):
    def wrapper(*args,**kw):
        start = time.time() # 记录开始时间

        result = func(*args,**kw) # 执行目标函数原有功能

        end = time.time() # 记录结束时间

        # 计算时间消耗
        duration = end-start
        print('函数%s耗时为：%s秒'%(func.__name__,duration))
        
        return result
    return wrapper

@decorator
def power(x):
    time.sleep(random.randint(0,3))
    return x*x

r = power(7)
print(r)



