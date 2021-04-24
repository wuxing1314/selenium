'''高级特性'''

'''
迭代iterate
迭代可以简单理解为循环

可迭代对象 - 可以进行迭代操作的对象
列表，字符串，range(10)...

'''

names = ['窦建辉','樊会喜','师亚贤','伍星','郭敏娜','曹晶晶','王家凯']

# 迭代
# range()
for i in range(10):
    print(i)

# 列表
for name in names:
    print(name)

# 字符串
for c in 'abcdef':
    print(c)

# 字典
classmates = {'窦建辉':89,'樊会喜':88,'师亚贤':91,'伍星':87,'郭敏娜':93,'曹晶晶':95,'王家凯':80}

# 迭代key
for key in classmates:
    print(key,classmates[key])

# 迭代value
for value in classmates.values():
    print(value)

# 同时迭代key和value
for k,v in classmates.items():
    print(k,v)

'''如何判断一个对象是可迭代对象'''

from collections.abc import Iterable

print(isinstance('abcd',Iterable))
print(isinstance(5,Iterable))


for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)