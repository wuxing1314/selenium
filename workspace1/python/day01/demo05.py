'''字符串和编码'''

# 编码
# 'a' -> 97
# 解码
#  97 -> 'a'

# ASCII American Standard Code for Information Interchange
# 位 bit 1 0
# 字节 byte 8个bit 就是一个byte 256 0-255

# GB2312  
# GBK

# unicode 一般是用2个字节表示一个字符 （4个）

print(bin(65))
'''
ascii
0100 0001

unicode
0000 0000 0100 0001

'''

# utf-8 对于英文和数字，用1个字节，对于汉字用通常3个字节

# 在内存中统一使用Unicode编码
# 在硬盘上使用utf-8或者gbk

# 乱码

# 查看编码
print(ord('中'))
print(ord('国'))

# 查看编码对应的字符
print(chr(66))
print(chr(20000))
print(chr(30000))

# 作业，自学进制转换函数
# bin()
# oct()
# hex()
# int()

'''格式化输出'''

name = input('请输入您的姓名：')
age = input('请输入您的年龄：')

'''占位符'''
# %s 字符串占位符
print('您的姓名是：%s,您的年龄是：%s'%(name,age))
# %d 整数占位符
print('您的姓名是：%s,您的年龄是：%d'%(name,int(age)))
# %f 浮点数占位符
PI = 3.1415926
print('PI=%.2f'%PI)

'''format()函数'''
print('您的姓名是：{0},您的年龄是：{1}'.format(name,age))
