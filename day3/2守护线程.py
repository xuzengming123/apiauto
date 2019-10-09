
import time,threading

# def foo(something,num):
#     for i in range(num):
#         print('CPU切换执行：',something)
#         time.sleep(1)

# #创建一个线程
# t1 = threading.Thread(target=foo,args=('注册账号',10))
# #再创建一个线程
# t2 = threading.Thread(target=foo,args=('登录账号',10))
#
# #启动线程
# t1.start()
'''阻塞父线程继续执行'''
# t1.join()
# t2.start()


#以下为守护线程的知识点
def foo(something,num):
    for i in range(num):
        print('CPU切换执行：',something)
        time.sleep(1)

#创建一个任务听音乐
t1 = threading.Thread(target=foo,args=('听音乐',3))
#再创建一个任务看电影
t2 = threading.Thread(target=foo,args=('看电影',3))

'''
    将线程声明为守护线程，必须在start()方法调用之前设置
    这个方法基本和join是相反的，当我们在程序运行中，执行一个主线程，如果主线程有创建一个子进程
    主线程和子线程 就兵分两路，分别运行，那么当主线程完成想退出时，会检验子线程是否完成
    如果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是 只要主线程完成了
    不管子线程是否完，都要和主线程一起退出，这时就可以用setDaemon方法
'''
#将听音乐设置为守护线程
#设置守护线程必须在 start 方法之前调用
t1.setDaemon(True)

#启动线程
t1.start()
t2.start()

print('主线程最后一行代码执行结束')