import os
import subprocess

# 阻塞式调用
# os.system("mspaint")
#
# print('after')

# subprocess.Popen('ipconfig')
# print('after')

# a = input()
# b = input()
# c = input()
# d = input()
#
# print("a=",a)
# print("b=",b)
# print("c=",c)
# print("d=",d)

subprocess.Popen(
    "python test1.py",
    stdin=subprocess.PIPE, #标准输入
)