import requests
from business.base_token import BaseToken
from config.parseconfig import data


class OA(BaseToken):
    def __init__(self,secret = data['contact_secret']):
        super().__init__(secret)

    def get_checkin_data(self,opencheckindatatype,starttime,endtime,useridlist:list):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata?access_token='+self.token
        data = {
            "opencheckindatatype": opencheckindatatype,
            "starttime": starttime,
            "endtime": endtime,
            "useridlist": useridlist
        }
        r = requests.post(url=url,data=data)
        return r

if __name__ == '__main__':
    print(OA().get_checkin_data().json())
