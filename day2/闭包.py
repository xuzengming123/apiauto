# def foo():
#     a = 'hello'
#     def bar():   # bar是一个内部函数
#         print(a)  # 在一个内部函数里面，引用外部作用域（不能是全局作用域）的变量
#     return  bar
#
# f = foo() #f==bar
#
# f()


import os.path
path = '/home/zikong/doc/file.doc'
print(os.path.basename(path))     # 查询路径中包含的文件名----file.doc
print(os.path.dirname(path))      # 查询路径中包含的目录-----/home/zikong/doc
info = os.path.split(path)        # 将路径分割成文件名和目录两个部分，放在一个表中返回
print(info)                       #----('/home/zikong/doc', 'file.doc')

path2 = os.path.join('\\','home','zikong','doc','file.doc')  #使用目录名和文件名构成一个路径字符串
print(path2)               #\home\zikong\doc\file.doc

p_list = [path, path2]
print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分