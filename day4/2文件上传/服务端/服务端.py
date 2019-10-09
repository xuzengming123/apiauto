# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/30

import socket,os

#创建 socket 对象
sk = socket.socket()
#绑定服务器地址
sk.bind(("127.0.0.1",13001))
#监听
sk.listen()


def get_file(sk_obj):
    '''
    接收文件
    :param sk_obj:socket对象
    :return:
    '''
    #接收文件大小
    file_size = int(sk_obj.recv(1024).decode('utf8'))
    #告诉对方我已经收到文件大小了
    sk_obj.sendall('ok,文件大小接收完毕'.encode('utf'))

    #接收文件名字
    file_name = sk_obj.recv(1024).decode('utf8')
    # 告诉对方我已经收到文件名字了
    sk_obj.sendall('ok,文件名字接收完毕'.encode('utf'))

    #接收文件
    with open('./%s' %file_name,'wb') as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size -= 1024

#等待传入连接,成功则返回
conn,addr = sk.accept()

get_file(conn)

conn.close()
sk.close()