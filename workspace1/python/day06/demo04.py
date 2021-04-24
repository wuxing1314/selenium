'''线程和进程'''

'''
进程 Process
一个程序至少有一个进程
复杂程序有多个进程

线程 Thread
一个进程里面至少有一个线程
复杂进程可以有多个线程
线程是CPU调度的最小的单位
'''

from multiprocessing import Process
import os

def run(name):
    print('运行子进程%s:%s'%(name,os.getpid()))

if __name__ == "__main__":
    print('父进程(主进程)%s'%os.getpid())
    # 创建子进程
    p = Process(target=run,args=('test',))  # run('test')
    p1 = Process(target=run,args=('test1',))  # run('test')
    p2 = Process(target=run,args=('test2',))  # run('test')

    print('子进程开始')
    p.start() # 启动子进程
    p1.start() # 启动子进程
    p2.start() # 启动子进程
    p.join() # 将子进程加入到父进程中
    p1.join() # 将子进程加入到父进程中
    p2.join() # 将子进程加入到父进程中
    print('子进程结束')

    print('父进程结束')