'''
模块 module
在Python中，一个文件就是一个模块
    -方便维护代码
    -方便代码重用
    -注意: 自定义模块名不要和系统模块名冲突
包-package(文件夹)
    -有一个__init__.py的模块
    -可以有效的避免模块命名冲突
    -方便代码的管理
    com.abc.python.day04.demo01
'''

'''使用模块'''

# 导入模块
import sys

def f():
    # argv--接收命令行参数,并封装为一个列表
    args = sys.argv
    if len(args)==1:
        print('Hello')
    elif len(args)==2:
        print('Hello , %s'%args[1])
    else:
        print('参数太多啦！')


'''作用域'''

# 公开的 public
def g():
    print('Hello')

# 私有的 private
def _h():
    print('Hi')

__abc = 'tom'

PI = 3.14

PI = -2

print(g.__name__)

'''
类似于__xxxx__形式的变量是特殊变量
'''


'''
安装第三方模块

查看已安装的模块
    pip list    
安装模块
    pip install 模块名      
设置镜像网站
    pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

'''


if __name__ == "__main__":
    f()

# f()
# f()