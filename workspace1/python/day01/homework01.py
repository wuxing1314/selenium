# 1. 作业-Zen of Python
#     在交互模式下输入 import this。查看并翻译结果


# 2. 作业，自学进制转换函数
#     bin()
#     oct()
#     hex()
#     int()

# 3. 输入张三2次的考试成绩，输出成绩提升百分比

# 4. 对列表scores = [89,88,91,87,93,95]进行增删改查的操作

# 5. 计算BMI指数（多分支结构）
#     bmi = 体重(kg)/身高(m)/身高(m)
#     <18.5  太瘦
#     18.5-25 正常
#     25-28   微胖
#     28-32   肥胖
#     >32     死肥宅

# 6.输出两个int数中的最大值
#     用户从控制台接收两个整数，通过程序找出两个数中的最大值。

# 7.编写程序判断某一个年份是否为闰年（使用if-else)
#     本案例需要使用交互的方式判断某年是否为闰年：用户从控制台输入需要判断的年份值，
#     由程序使用if-else判断该年是否为闰年，并将判断结果输出到控制台。

# 8.输出三个int数中的最大值
#     用户从控制台接收三个整数，通过程序找出三个数中的最大值。
a = int(input('First：'))
b = int(input('Second：'))
c = int(input('Third：'))

max = a
if max < b:
    max = b
elif max < c:
    max = c
print('max=%d'%max)