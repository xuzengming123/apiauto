with open("C:/Users/29276/Desktop/gbk编码.txt",encoding='gbk') as f1,\
open("C:/Users/29276/Desktop/utf8编码.txt",encoding='utf8') as f2:
    data = f1.read()
    data1 = f2.read()
    print(data1)

content = data+','+data1   #李老师年龄：32,张老师年龄：28


'''
   程序用中文提示用户“请输入 新文件的名称”，
   用户输入文件名可以包含中文
   将上面合并后的内容存储到一个新文件中，以utf8格式编码。
   新文件的文件名就是上面用户输入的名字。
'''

filename = input('请输入 新文件的名称：')
with open(f'./{filename}','a',encoding='utf8') as newfile:
    newfile.write(content)
    newfile.close()