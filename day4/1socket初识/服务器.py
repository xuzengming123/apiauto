# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/30

import socket


ip_port = ("127.0.0.1",13000)   #服务器的IP和端口号

#创建 socket 对象
sk = socket.socket()

#绑定IP地址和端口号，调用bind()方法,接收的是元组！！
sk.bind(ip_port)

#监听，看有没有请求过来
sk.listen(5)  #最多同时接收5个
print("服务端启动了")




#等待传入连接
#连接成功之后，返回一个新的 socket 对象，并且会返回客户端的IP地址和端口号
conn,addr = sk.accept()   #等待传入连接,成功则返回
print('客户端的地址：',addr)


#接收客户端的数据
client_data = conn.recv(1024)
print(client_data.decode('utf8'))

'''服务器接收数据后开始处理，处理结束后返回数据到客户端'''

send_data = input('请输入>>>')
#发送数据到客户端
conn.sendall(send_data.encode('utf8'))


#释放资源
conn.close()
sk.close()






















