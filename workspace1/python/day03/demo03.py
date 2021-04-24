'''高级特性'''

'''
列表生成式
'''
l = [1,2,3,4,5,6,7,8]
m = list(range(101))

# [1*1,2*2,3*3,4*4,...10*10]
# 方法1 - 循环
n = []
for i in range(1,11):
    n.append(i*i)
print(n)

# 方法2 - 列表生成式
p = [i*i for i in range(1,11)]
print(p)

# 列表生成式中开可以添加过滤条件
q = [i*i for i in range(1,11) if i%2==0]
print(q)

r = [i+j for i in 'abc' for j in 'xyz']
print(r)

