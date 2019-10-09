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


print('\n')
print('---第1步列出课程')
courseListBefore = student.list_course(1,20,sessionid)['retlist']



print('\n')
print('---第2步删除课程')
retObj = student.delete_course(courseListBefore[0]['id'],sessionid)
print(retObj)
try:
    retObj['retcode'] == 0
    print('删除成功')
except:
    print('删除失败')



print('\n')
print('---第3步列出课程')
courseListAfter = student.list_course(1,20,sessionid)['retlist']


del_course = None
for one in courseListBefore:
    if one not in courseListAfter:
        del_course = one
print('刚刚删除的课程',del_course)

assert del_course!=None
assert del_course['name']==courseListBefore[0]['name']
assert del_course['desc']==courseListBefore[0]['desc']
assert del_course['display_idx']==courseListBefore[0]['display_idx']

print('\n========= test case pass =============')