'''
Output
w : 以覆盖方式写文本文件
a : 以追加方式写文本文件
b : 二进制
wb: 以只读方式读取二进制文件
'''

with open(r'python\day06\demo.txt','w',encoding='utf-8') as f:
    f.write('人生苦短，对酒当歌。\n')
    f.write('人生苦短，我用python。')

# 练习：复制test.txt中的内容到demo.txt中
