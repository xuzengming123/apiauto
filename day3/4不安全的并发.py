# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/28

import threading,time,random


account_balance = 500   #银行卡余额
r = threading.Lock()  #Lock()方法返回一把锁

def option_blance(num):
    #操作账户余额
    # 声明全局变量
    global account_balance

    '''重要的数据操作，上锁！！！'''
    r.acquire()

    # 把接口获取到的值存入到自己的系统
    balance = account_balance
    time.sleep(random.randint(0,10)*0.1) #模拟接口响应时间，模拟计算时间
    balance += num

    '''数据操作结束，解锁！！！'''
    r.release()

    # 计算结束后，将结果传递回去
    account_balance = balance


# 支付宝那边的线程
t1 = threading.Thread(target=option_blance,args=(-300,))
# 银行这边的线程
t2 = threading.Thread(target=option_blance,args=(10000,))

#启动线程
t1.start()
t2.start()
t1.join()
t2.join()

print('所有子线程执行完毕')
print('最终余额：',account_balance)


