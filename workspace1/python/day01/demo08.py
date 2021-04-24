'''
分支结构

程序的3中结构：
1.顺序结构
2.分支结构
3.循环结构

解释型语言
编译型语言
'''

age = int(input('请输入您的年龄：'))

'''
多分支结构：

if 必须有，并且只能有一个
elif 可以没有，也可以有多个
else 可以没有，但是有的话只能有一个
所有的分支都是排他的(exclusive)，也就是说无论如何，只能有一个分支被执行
'''
if age<18:
    print('未成年')
elif age>=18 and age<35:
    print('青年')
elif age>=35 and age<55:
    print('中年')
else:
    print('老年')

print('over!')
