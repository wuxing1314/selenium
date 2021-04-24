'''函数的参数'''


'''
1.位置参数 positional argument
-位置参数在调用时，按照参数的顺序依次传参
-位置参数在调用时，必须传参
'''
# 求x的平方
# 命名时要遵循 见名知意 的原则
def power(x): # verion 1.0
    return x*x

print(power(9))
# print(power())

# 求x的n次方
def power2(x,n):
    s = 1
    while n>0:
        s = s*x
        n = n -1
    return s

print(power2(2,3))
print(power2(2,2))

'''
2. 默认参数
-默认参数有一个默认值
-默认参数必须放在位置参数的后面
-默认参数可以降低函数调用的难度
-默认参数在传参时，默认按照顺序传参，也可以按照参数名传参
'''
def power3(x,n=2):
    return x**n

print(power3(7))
print(power3(5,3))

def info(name,age,gender='男',city='西安'):
    print(name,age,gender,city)

info('tom',22,'男','西安')
info('mike',25)
info('julia',18,'女','贵阳')
# 西安人，女生
info('stella',17,gender='女')
# 成都人，男生
info('henry',22,city='成都',gender='男')

'''
3.可变参数
-将所有传入的参数打包成一个元组
-可以传参数，也可以不传参数，
-可以传任意个参数
'''
# 求一组数字的和
l = [1,7,13,-5,0,22]

def f(*nums): # 打包
    print('nums=',nums)
    s = 0
    for i in nums:
        s = s + i
    return s

print(f(1,7,13,-5,0,22,3,2,1,-7))

print(f(l[0],l[1],l[2],l[3],l[4],l[5]))
print(f(*l)) # 拆包


'''
4.关键字参数
-将所有传入的参数封装为一个字典
-可以传参数，也可以不传参数，
-可以传任意个参数
'''

def info2(name,age,**kw):
    print(name,age,kw)

info2('tom',20)
info2('tom',20,gender='Male',hobby='农药')
info2('tom',20,gender='Male',hobby='农药',city='上海')

'''
5.命名关键字参数 keyword-only arguments
'''
def info3(name,age,*,gender,city):
    print(name,age,gender,city)

info3('tom',22,gender='Male',city='西安')

def m(*args,**kw):
    pass

