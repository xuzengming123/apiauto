# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/28

import threading,time,random

num_list = [] #存放包子

def producer():
    global num_list  # 引用全局变量
    #生产者
    while True:  #生产者不停的生产包子


        if loak_con.acquire():
            num_list.append(1)
            print("生产者生产了一个包子",num_list)

            loak_con.notify_all() #通知所有等待的人来吃包子
            loak_con.release()

            #模拟包子端上桌子的时间
            time.sleep(random.randint(0,10)*0.1)

def consumer():
    global num_list #引用全局变量
    #消费者
    while True:  #不停的吃包子
        if loak_con.acquire():
            if len(num_list) == 0:
                print('没有包子吃')
                #线程进入等待池
                loak_con.wait()

            #有包子吃的时候
            num_list.remove(num_list[0])
            print('消费者吃掉了一个包子',num_list)

            #模拟吃掉包子花费的时间
            time.sleep(random.randint(0,10)*0.1)
            loak_con.notify_all()  #通知大家来吃包子
            loak_con.release()


loak_con = threading.Condition()  #条件锁对象

t1 = threading.Thread(target=producer)  #生产者
t2 = threading.Thread(target=consumer)  #消费者

t1.start()
t2.start()