'''调用栈 call stack'''

'''
调试代码：
    -print() 打印相关变量
    -debug调试工具
'''
x = 5

def f(s):
    a = 3
    b = 'abc'
    print('s=',s)
    s = int(s)
    return 10/s

def g(s):
    return f(s)*2

def m():
    try:
        g('0')
    except Exception as e:
        print(e)  # 记录了异常信息
        # 手动抛出异常
        raise NameError('发生异常了!')
# def m():
#     g('0')

'''
最终把异常抛给Python解释器
Python 解释器处理异常的标准方式：
-打印 调用栈 信息
-杀死程序
'''
m()     

'''
调用栈：

Traceback (most recent call last):
  File "d:/workspace/python/day05/demo04.py", line 11, in <module>
    m()
  File "d:/workspace/python/day05/demo04.py", line 9, in m
    g('0')
  File "d:/workspace/python/day05/demo04.py", line 6, in g
    return f(s)*2
  File "d:/workspace/python/day05/demo04.py", line 3, in f
    return 10/int(s)
ZeroDivisionError: division by zero
'''