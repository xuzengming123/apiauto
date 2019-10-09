import requests
from pprint import pprint
from cfg import *
from libs.apilibs import *
import time

student = CourseMgr()
print('---Login---')
loginRet,cookies = student.login('auto','sdfsdfsdf')
try:
    assert loginRet['retcode'] == 0
    print('登录成功')
except:
    print('登录失败')
#记录sessionid
sessionid = cookies['sessionid']



print('\n')
coursename = 'perl_'+ str(round(time.time() * 1000))
print('-----第1步，先添加1门课程')
addRet = student.add_course(coursename,'perl课程','5',sessionid)
print('---检查点==》检查返回消息体---')
try:
    assert addRet['retcode']  == 0   #关键字assert,不通过就报错
    print('返回结果：retcode为0，检查通过')
except:
    print('！！返回结果：retcode不为0，检查不通过')


print('\n')
print('-----第2步，先列出课程')
courseListBefore = student.list_course(1,20,sessionid)['retlist']

print('\n')
print('-----第3步，添加1门课程')
addRet = student.add_course(coursename,'perl课程','5',sessionid)
try:
    assert addRet['retcode'] == 2
    print('该课程已存在')
except:
    print('该用例失败')

print('\n')
print('-----第4步，再列出课程')
courseListAfter = student.list_course(1,20,sessionid)['retlist']

assert courseListBefore == courseListAfter

print('\n========= test case pass =============')
