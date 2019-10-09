# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/30

import socket,os

#创建socket对象
sk = socket.socket()

#连接服务器
sk.connect(("127.0.0.1",13001))


def post_file(sk_obj,file_path):
    '''
    上传文件
    :param sk_obj: socket 对象
    :param file_path: 文件的路径
    :return:
    '''
    #获得文件大小
    file_size = os.stat(file_path).st_size
    #发送文件
    sk_obj.sendall(str(file_size).encode('utf8'))

    sk_obj.recv(1024)


    #获取文件名称
    file_name = os.path.split(file_path)[1].encode('utf8')
    #发送文件名称
    sk_obj.sendall(file_name)
    sk_obj.recv(1024)

    #发送文件内容
    with open(file_path,'rb') as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size -= 1024

path ='C:/Users/29276/PycharmProjects/apiauto\day4/2文件上传/客户端/qqjt.txt'
post_file(sk,path)

sk.close()













