'''进程池'''

from multiprocessing import Pool
import os,time,random

def task(name):
    print('运行任务%s:%s'%(name,os.getpid()))
    time.sleep(random.randint(5,10))

if __name__ == "__main__":
    print('父进程%s'%os.getpid())
    # 创建进程池
    pool = Pool(20) # 默认创建4个进程
    for i in range(10):
        pool.apply_async(task,args=(i,)) # asynchronous 异步

    pool.close()
    pool.join()
    print('所有子进程执行结束')