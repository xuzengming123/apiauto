# print(ord('甜'))
# print(ord('苦'))
# print(ord('a'))
#
#
# print(chr(29980))
# 声明一个变量，类型是str类型
a ='海日生残夜，江春入旧年'  #str -->bytes
# 把str类型转换为bytes类型的两种方式
print(bytes(a,encoding='utf8'))
print(a.encode('utf8'))


# 声明一个类型，类型是bytes类型
b = b'\xe6\xb5\xb7\xe6\x97\xa5\xe7\x94\x9f\xe6\xae\x8b\xe5\xa4\x9c\xef\xbc\x8c\xe6\xb1\x9f\xe6\x98\xa5\xe5\x85\xa5\xe6\x97\xa7\xe5\xb9\xb4'
# 把bytes类型转换为str类型的两种方式
print(str(b,'utf8'))
print(b.decode('utf8'))