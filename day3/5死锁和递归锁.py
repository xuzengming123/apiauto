# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/28
import threading,time

# lockA = threading.Lock() #小明的锁
# lockB = threading.Lock() #面试官的锁
#
#
# # 面试官的逻辑
# def foo1():
#     lockA.acquire()
#     print('请解释什么是死锁')  #请求小明的资源0
#     time.sleep(1)
#
#     lockB.acquire()
#     print('发 offer')
#     time.sleep(1)
#
#     lockB.release() #面试官解锁
#     lockA.release() #小明的锁
#
#
# #小明的逻辑
# def foo2():
#     lockB.acquire()
#     print('请给我发 offer')  #请求面试官的资源
#     time.sleep(1)
#
#     lockA.acquire()
#     print('给面试官解释什么是死锁')
#     time.sleep(1)
#
#     lockA.release() #小明的锁
#     lockB.release() #面试官解锁




rLock = threading.RLock()   #可重入锁

# 面试官的逻辑
def foo1():
    rLock.acquire()
    print('请解释什么是死锁')  #请求小明的资源0
    time.sleep(1)

    rLock.acquire()
    print('发 offer')
    time.sleep(1)

    rLock.release() #面试官解锁
    rLock.release() #小明的锁


#小明的逻辑
def foo2():
    rLock.acquire()
    print('请给我发 offer')  #请求面试官的资源
    time.sleep(1)

    rLock.acquire()
    print('给面试官解释什么是死锁')
    time.sleep(1)

    rLock.release() #小明的锁
    rLock.release() #面试官解锁


t1 = threading.Thread(target=foo1)

t2 = threading.Thread(target=foo2)
t1.start()
t2.start()


