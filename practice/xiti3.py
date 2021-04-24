'''
输入某年某月某日，判断这一天是这一年的第几天？
以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天
'''

y = int(input('year:\n'))
m = int(input('month:\n'))
d = int(input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0< m <=12:
    sum = months[m-1]
else:
    print('date error')
sum += d
leap = 0
if