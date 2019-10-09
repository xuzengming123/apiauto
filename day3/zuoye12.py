# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/29

import threading,requests
from pprint import pprint

url1 = 'http://mirrors.163.com/centos/6/isos/x86_64/README.txt'
url2 = 'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt'
urls = ['http://mirrors.163.com/centos/6/isos/x86_64/README.txt','http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt']
r = threading.Lock()  #Lock()方法返回一把锁
fileContentList = [None for one in urls]
def get_txt(idx,url):
    #获取文本内容
    print('thread #%s start' % idx)
    ret = requests.get(url)
    r.acquire()
    fileContentList[idx] = ret.text
    r.release()
    print('thread #%s end' % idx)

# t1 = threading.Thread(target=get_txt,args=(url1,))
# t2 = threading.Thread(target=get_txt,args=(url2,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

for one in urls:
    t = threading.Thread(target=get_txt, args=(one,))
    t.start()
    t.join()
pprint(fileContentList)
