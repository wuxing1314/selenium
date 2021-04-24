'''
字典 dict
字典是无序的
key是不可以重复的
value是可以重复的
'''

names = ['窦建辉','樊会喜','师亚贤','伍星','郭敏娜','曹晶晶','王家凯']
scores = [89,88,91,87,93,95,80]

# 创建一个字典
# 键-值对 key-value
classmates = {'窦建辉':89,'樊会喜':88,'师亚贤':91,'伍星':87,'郭敏娜':93,'曹晶晶':95,'王家凯':80}

# 查询
print(classmates['郭敏娜'])

# 添加数据
classmates['雷鸣'] = 88
print(classmates)

# 修改数据
classmates['雷鸣'] = 89
print(classmates)

# 删除数据
score = classmates.pop('窦建辉')
print(score)
print(classmates)

if '窦建辉' in classmates:
    classmates.pop('窦建辉')

print(classmates)

classmates = {'窦建辉':{'python':89,'math':90},'樊会喜':88,'师亚贤':91,'伍星':87,'郭敏娜':93,'曹晶晶':95,'王家凯':80}
score = classmates['窦建辉']['python']
print(score)