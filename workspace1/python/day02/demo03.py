'''函数'''
PI = 3.1415926
s = PI * 10 * 10
s1 = PI * 20 * 20
# ax2+bx+c = 0

# 内置函数

print() # 调用函数
abs(-5) # 调用求绝对值函数

'''
定义函数
def 定义函数的关键字
x 形式参数 - 形参
return 返回函数执行的结果，立即结束函数的执行
'''
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

# 调用函数
# -5 是实际参数-实参
print(my_abs(-5))

'''空函数'''
def f():
    pass

'''函数返回多个值'''
import math     # 导入模块math
def g(x,y,angle):
    nx = x * math.sin(angle)
    ny = y * math.cos(angle)
    return nx,ny  # 只能返回一个值

# x = g(1,2,3.1415926/6)[0]
# y = g(1,2,3.1415926/6)[1]
x,y = g(1,2,3.1415926/6)
print(x,y)