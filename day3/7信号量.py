# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/28

import threading,time,random

# 规定停车场的数量
semaphore = threading.BoundedSemaphore(4)

def foo(i):

    semaphore.acquire() #每次加锁，停车位减1
    print('这是第%s个'%i)
    time.sleep(random.randint(0,10))
    print('停车位释放')
    semaphore.release()   #每次解锁，停车位加1

for i in range(20):
    t = threading.Thread(target=foo,args=(i,))
    t.start()










