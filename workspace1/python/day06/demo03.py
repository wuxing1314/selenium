'''操作文件和目录'''

import os

# 系统名称
print(os.name) # nt Windows NT
# 系统环境变量
# print(os.environ) # enrironment
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.')) # workspace

# 创建一个目录
# os.mkdir('./a/b')

# 创建多个目录
os.makedirs('./a/b/c')

print(os.listdir('.'))
# 列出当前目录下的所有目录
m = [dir for dir in os.listdir('.') if os.path.isdir(dir)]
print(m)
# 列出当前目录下的所有文件
n = [dir for dir in os.listdir('.') if os.path.isfile(dir)]
print(n)
