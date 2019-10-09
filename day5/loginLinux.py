# -*- coding: utf-8 -*-
# __author__:29276
# 2019/9/1

import paramiko

#创建ssh对象
ssh = paramiko.SSHClient()

#设置联系方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#开始连接远程主机（IP地址，端口号，用户名，密码）
ssh.connect("192.168.2.106",22,"root","sdfsdf")

#开始在远程机器上执行命令
stdin,stdout,stderr = ssh.exec_command('ifconfig')
print(stdout.read())


#创建一个客户端，可以进行文件传输
sftp = ssh.open_sftp()

#将本地的文件传输到远程机器
sftp.put("本地文件路径","远程机器文件路径")

#将远程机器的文件下载到本地
sftp.put("远程机器文件路径","本地文件路径")

sftp.close()
ssh.close()


#hahahahahha