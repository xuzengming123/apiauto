# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/28

import time,threading
# def foo(something):
#     print(something)
#     time.sleep(1)
#
# # 串行的方式
# begin_time = time.time()
# foo('磁盘接收100M数据')
# foo('CPU 去做其他的事情')
# end_time = time.time()
#
# print('执行时间：',end_time-begin_time)
#
# # 并行的方式
# begin_time = time.time()
# t1 = threading.Thread(target=foo,args=('磁盘接收100M数据',))
# t2 = threading.Thread(target=foo,args=('CPU 去做其他的事情',))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time = time.time()
#
# print('执行时间：',end_time-begin_time)





def bar():
    num = 0
    for i in range(1000000):
        num += 1


# 串行的方式
begin_time = time.time()
bar()
bar()
end_time = time.time()
print('执行时间：',end_time - begin_time)


# 并行
begin_time = time.time()
t1 = threading.Thread(target=bar)
t2  =threading.Thread(target=bar)
t1.start()
t2.start()
# 添加join---目的是阻塞主线程，不加程序会直接执行58行
t1.join()
t2.join()
end_time = time.time()
print('执行时间：',end_time - begin_time)