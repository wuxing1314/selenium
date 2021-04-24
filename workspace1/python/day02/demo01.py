'''循环结构'''

# 1+2+3+4+5+6+7+8+9+10
s = 1+2+3+4+5+6+7+8+9+10
print('s=%d'%s)

'''for循环'''
s = 0
for i in [1,2,3,4,5,6,7,8,9,10]:
    s = s + i
'''
i = 1  s = 0+1 = 1
i = 2  s = 1+2 = 3
i = 3  s = 3+3 = 6
...

i = 10 s = 45 + 10 = 55
end


'''
print('s=%d'%s)

r = list(range(11))
print(r)

s = int('1')+int('2')
print(s)

s = 0
for i in range(101):
    s = s + i
print('s=%d'%s)

print('-------------------------------')

'''while循环'''
# 1+2+3+4+5+6+7+8+9+10
s = 0
i = 1
while i<=100:
    s = s + i
    i = i + 1
print('s=%d'%s)

# 求100以内所有奇数的和
s = 0
i = 1
while i<=100:
    if i%2 !=0:
        s = s + i
    i = i + 1
print('s=%d'%s)

'''break语句'''
# 当和大于1000时退出循环
s = 0
i = 1
while i<=100:
    if s>= 1000:
        #退出循环
        break  # 中断循环
    s = s + i
    i = i + 2
print('s=%d'%s)

'''continue语句'''
s = 0
i = 0
while i<100:
    i = i + 1
    if i%2 == 0:
        continue  # 中断本次循环
    s = s + i
print('s=%d'%s)

# 使用for循环打印100以内的所有偶数
for i in range(100):
    if i%2 == 0:
        print(i)


