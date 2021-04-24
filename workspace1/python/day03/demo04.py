'''高级特性'''

'''
生成器 generator
'''

l = [i*i for i in range(11)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l)

# 生成器
g = (i*i for i in range(11))
# <generator object <genexpr> at 0x0000000001DE7AC0>
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
    print(i)


# Fibonacci数列
# 1 1 2 3 5 8 13...

def fib(n):
    m,a,b = 0,0,1
    while m<n:
        # print(b)
        yield b  # 类似于 return b，返回b的值，但是不会结束函数
        # t = a
        # a = b
        # b = t+b
        a,b = b,a+b
        m = m+1
'''
m a b   print(b)  a b m
0 0 1       1     1 1 1
1 1 1       1     1 2 2
2 1 2       2     2 3 3
3 2 3       3     3 5 4


'''
print('----------------------------------')
# <generator object fib at 0x0000000002437AC0>
n = fib(7)


# for i in n:
#     print(i)

# 真.斐波那契数列
def fibonacci():
    a,b = 0,1
    while True:
        yield b  # return b
        a,b = b,a+b

fibo = fibonacci()

import time

for i in fibo:
    print(i)
    time.sleep(1)

