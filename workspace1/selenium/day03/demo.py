'''
输入： 两个n 位正整数x 和y .
输出： x 和y 的乘积。
先决条件： n 是2 的整数次方。
'''

def f(x,y):
    x = str(x)
    y = str(y)
    n = len(x) 
    if n == 1: #终止递归
        return int(x)*int(y)
    else:   
        a,b= x[:int(n/2)], x[int(n/2):]
        c,d= y[:int(n/2)], y[int(n/2):]
        ac,ad,bc,bd = f(a,c),f(a,d),f(b,c),f(b,d)
        return ac*10**n +(ad+bc)*10**(n/2)+bd

print(f(1234,5678))
print(1234*5678)
