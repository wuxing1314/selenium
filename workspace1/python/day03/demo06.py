'''函数式编程'''


'''装饰器'''
import time

# def now():
#     print(time.strftime('%Y-%m-%d'))

# now()

# print(now.__name__)
# f = now
# print(f.__name__)

# 定义一个装饰器
def log(func):
    def wrapper(*args,**kw):
        print('调用函数%s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

# now = log(now)
# now()

@log
def now():
    print(time.strftime('%Y-%m-%d'))

now()

@log
def f(x):
    print('%d*%d=%d'%(x,x,x*x))


f(3)

print('-------------------------------')
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func) # 将函数wrapper的__name__的值修改为func.__name__
        def wrapper(*args,**kw):
            # wrapper.__name__ = func.__name__
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


@log('执行')
def now2():
    print(time.strftime('%Y-%m-%d'))

now2()
print(now2.__name__)