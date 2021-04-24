'''
异常处理

异常处理机制
try...except...finally..
'''

try: # 把有可能出错的代码放在try代码块中
    n = int(input('请输入一个整数:'))

    result = 100/n

    print('result=%s'%result)
# 当捕捉多个异常时，子类在前面，父类在后面
except ZeroDivisionError as e: # 捕捉异常
    print('发生了ZeroDivisionError错误：',e)
    # raise NameError('出错了')  # 手动抛出异常
except ValueError as e: # 可以捕捉多个异常
    print('发生了ValueError错误：',e)
except Exception as e:
    print('发生了Exception错误',e)
finally: # 无论如何都会执行
    print('关闭数据库！')

print('程序执行结束啦！')