from business.base_token import BaseToken
import requests
from config.parseconfig import data

class UserManage(BaseToken):

    def get_department(self,id= None):
        params = {
            'access_token':self.token,
            'id':id
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'

        r = requests.get(url=url,params=params)
        return r

    def get_user(self,department_id,fetch_child=1):
        params = {
            'access_token':self.token,
            'department_id':department_id,
            'fetch_child':fetch_child
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist'
        r = requests.get(url=url,params=params)
        return r

if __name__ == '__main__':
    um = UserManage(data['checkin_secret'])
    d1 =um.get_department()
    print(d1.json())
    id = d1.json()['department'][0]['id']
    # print(id)
    u2 = um.get_user(id)
    print(u2.json())