# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/30

import socket


#创建一个socket对象
sk = socket.socket()

#连接服务器
sk.connect(("127.0.0.1",13000))   #服务器的IP和端口号



send_data = input('请输入>>>')
#发送数据到服务端
sk.sendall(send_data.encode('utf8'))


#接收数据
client_data = sk.recv(1024)
print(client_data.decode('utf8'))

#

