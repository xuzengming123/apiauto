import requests
from pprint import pprint
from cfg import *
class CourseMgr:
    def login(self,username,password):
        '''登录'''
        res = requests.post(f'http://{API_SERVER}/api/mgr/loginReq',
                            data={
                                "username":username,
                                "password":password,
                            })
        retObj = res.json()
        return retObj,res.cookies


    def add_course(self,name,desc,idx,sessionid):
        '''添加课程'''
        res = requests.post(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                      data={
                          'action':'add_course',
                          'data':'''
                          {
                          "name":"%s",
                          "desc":"%s",
                          "display_idx":"%s"}'''%(name,desc,idx)
                      },
                      cookies={"sessionid":sessionid})
        retObj = res.json()
        pprint(retObj)
        return retObj


    def list_course(self,pagenum,pagesize,sessionid):
        '''列出课程'''
        res = requests.get(f'http://{API_SERVER}/api/mgr/sq_mgr/',
                           params={
                               "action":"list_course",
                               "pagenum":pagenum,
                               "pagesize":pagesize,
                           },
                           cookies={"sessionid":sessionid}
                           )
        retObj = res.json()
        print(retObj)
        return retObj

    def modify_course(self,courseid,name,desc,displayidx,sessionid):
        pl = {
            'action': 'modify_course',
            'id' : courseid,
            'newdata' : f'''
                    {{
                      "name":"{name}",
                      "desc":"{desc}",
                      "display_idx":"{displayidx}"
                    }}
            '''
        }
        reponse = requests.put('http://localhost/api/mgr/sq_mgr/',
                                data=pl,
                                cookies={'sessionid': sessionid})
        retDict = reponse.json()
        return retDict



    def delete_course(self,courseid,sessionid):
        payload = {
            'action': 'delete_course',
            'id': f'{courseid}'
        }

        response = requests.delete("http://localhost/api/mgr/sq_mgr/",
                                   data=payload,
                                    cookies={'sessionid': sessionid})
        r = response.json()
        return r


