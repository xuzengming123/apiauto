import time,threading

import time
def foo(something,num):
    for i in range(num):
        print('CPU切换执行：',something)
        time.sleep(1)

#创建一个线程
t1 = threading.Thread(target=foo,args=('看电影',3))
#再创建一个线程
t2 = threading.Thread(target=foo,args=('听音乐',6))


#启动线程
t1.start()
t2.start()
print(t1)
print(t2)
