# -*- coding: utf-8 -*-
# __author__:29276
# 2019/8/30

import socket

#创建socket对象
sk = socket.socket()

#绑定IP地址和端口号
sk.bind(("127.0.0.1",13002))

#监听
sk.listen(5)
print("女神上线，并且还发了一条朋友圈")


while True:
    print("女神空闲了。。。。。。")

    #接收一个客户端连接
    conn,addr = sk.accept()
    print('有人来找女神聊天了：',addr)

    while True:
        try:
            client_data = conn.recv(1024)
            if not client_data:raise Exception("收到空数据")
        except:
            print("意外中断")
            break
        #处理消息
        client_data = client_data.decode('utf8')
        if client_data == 'exit':break
        print(client_data)

        #回复消息
        server_data = input("请输入>>>")
        conn.sendall(server_data.encode('utf8'))
