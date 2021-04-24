'''
线程 Thread
执行程序的基本单元

多线程安全问题 
Lock 上锁

线程池

Python多任务应选择多进程
GIL锁

ACID
atomic   原子性
consistence  一致性
isolation 隔离性
duration 持久性
'''

import threading,time,os


def run():
    print('线程%s正在运行...%s'%(threading.current_thread().name,os.getpid()))
    time.sleep(5)
    print('线程%s结束...%s'%(threading.current_thread().name,os.getpid()))


print('线程%s正在运行...%s'%(threading.current_thread().name,os.getpid()))

# 创建线程
t = threading.Thread(target=run,name='test')
# 启动线程
t.start()
t.join()
print('线程%s结束...%s'%(threading.current_thread().name,os.getpid()))