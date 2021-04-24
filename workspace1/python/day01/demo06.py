'''列表 list'''


# 创建列表
# 列表中的每一个值也叫做列表的元素 element
# 列表是一个有序集合,下标从0开始

# 下标index   0       1       2       3       4       5
names = ['窦建辉','樊会喜','师亚贤','伍星','郭敏娜','曹晶晶']
scores = [89,88,91,87,93,95]
# 列表的元素没有限制，可以存任意类型的元素
temp = ['tom',89,3.14,True]

# 操作数据
# 获取列表长度（列表中元素的个数）
length = len(names)
print('names的长度是：%d'%length)

# 获取列表中的元素
print(names[0])
print(names[5])

print(names[length-1])
print(names[-1]) # 倒数第一个
print(names[-6])
# print(names[-7]) # IndexError: list index out of range

# 向列表中添加元素
# append() 向列表末尾添加元素
names.append('栗嘉兴')
print(names)
names.append('雷鸣')
print(names)

# insert() 向指定的位置插入元素
names.insert(2,'李钊')
print(names)

# 删除元素
# pop() 删除并返回列表的最后一个元素
name = names.pop()
print(name)
print(names)

# pop(i) 删除并返回指定下标的元素
name = names.pop(4)
print(name)
print(names)

# 修改元素
names[1] = '段亚琴'
print(names)

# 空列表
l = []

# 二维列表
m = [[1,2],[3,4],[5,6]]

# 元组是否真的不可变？