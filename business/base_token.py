import requests
from config.parseconfig import data


class BaseToken:

    def __init__(self,SECRET):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params ={
            'corpid':data['compid'],
            'corpsecret':SECRET
        }
        r = requests.get(url=url,params=params)
        print(r.json())
        self.token = r.json()['access_token']

if __name__ == '__main__':
    BaseToken('gPo9q2e_9qmsDxcGnrPfCxWjRcaiE3nv2XTFzFrneKs')