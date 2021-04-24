'''
IO
Input/Output
'''


'''
Input
r : 以只读方式读取文本文件
b : 二进制
rb: 以只读方式读取二进制文件
'''

# 绝对路径 - 从盘符开始写的路径就是绝对路径
# open('D:\workspace\python\day06\test.txt')
# 相对路径 - 相对于 当前路径 的路径

try:
    # 打开文件
    f = None
    f = open(r'python\day06\test.txt',mode='r',encoding='utf-8')

    # 读取文件内容
    data = f.read()

    print(data)
finally:
    # 关闭文件
    if f: # False,None,0,'' 全部当做False，其余所有值当做True
        f.close()


print('--------------------------------------------')
'''
read() ：一次性读入文件的全部内容
readline(): 每次读取一行
readlines(): 一次性读入文件的全部内容，然后以行为单位封装为一个列表

mode: 打开方式
encoding:  字符编码集，默认使用操作系统的编码集
'''

# 使用with open...结构，不用进行异常处理，也不用调用close()方法
with open(r'python\day06\test.txt',mode='r',encoding='utf-8') as f:
    # data = f.read()
    # print(data)
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    print(f.readlines())
    
print('--------------------------------------------')

# 以二进制方式读取文件
with open(r'python\day06\test.txt',mode='rb') as f:
    data = f.read()
    print(data)


