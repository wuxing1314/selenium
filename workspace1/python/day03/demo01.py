'''高级特性'''
'''
切片slice
names(start:end:step)
start: 起始元素下标(包含)
end: 结束元素下标(不包含)
step: 步长

列表，元组，字符串都适用于切片操作
'''
names = ['窦建辉','樊会喜','师亚贤','伍星','郭敏娜','曹晶晶','王家凯']
# 获取列表的前三个元素 - 复制操作
# 前闭后开
l = names[0:3]
print(l)
print(names)

print(names[2:5])
# 获取最后3个元素
print(names[-3:])

print(names[:3])
# 复制整个列表
print(names[:])

m = names
n = names[:]
print(m)
print(n)

o = list(range(100))
print(o)

# 所有的偶数
# 2 是步长step，表示每2个数取一个
print(o[::2])
print(o[50::5])