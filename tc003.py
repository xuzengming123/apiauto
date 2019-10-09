import requests
import copy
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

# 先列出课程
print('\n')
print('-----第1步，先列出课程')
courseListBefore = student.list_course(1,20,sessionid)['retlist']

print('\n')
print('-----第2步，修改1门课程')
coursename = 'c++_'+ str(round(time.time() * 1000))
modifyRet = student.modify_course(courseListBefore[0]['id'],coursename,'c++课程','1',sessionid)
print(modifyRet)
try:
    assert modifyRet['retcode'] == 0
    print('修改成功')
except:
    print('修改失败')

print('\n')
print('-----第3步，再列出课程')
courseListAfter = student.list_course(1,20,sessionid)['retlist']

n = []
# 列出修改后的所有课程名
for i in courseListBefore:
    n.append(i['name'] )
if courseListAfter[0]['name'] in n:
    print('该课程已存在')
else:
    print('修改后的课程名在系统中不存在')
    print('\n========= test case pass =============')


