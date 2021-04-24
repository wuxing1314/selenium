'''
递归函数 Recursion
-一定是自己调用自己
-一定要有边界条件

优点：
    结构简单，逻辑清晰
缺点：
    执行效率低，受递归栈限制
    (尾递归-递归优化)

'''


'''
计算n! = 1*2*3*....*(n-1)*n
n! = n*(n-1)!
'''
def factorial(n):
    s = 1
    for i in range(1,n+1):
        s *= i  # s = s * i
    return s

print(factorial(3))
print(factorial(5))
print(factorial(1000))

# 递归函数
def factorial2(n):
    if n == 0: # 2.边界条件-结束递归调用的条件
        return 1
    return factorial2(n-1)*n # 1.自己调用自己-递归

print(factorial2(3))
print(factorial2(5))
print(factorial2(1000)) #RecursionError: maximum recursion depth exceeded in comparison

