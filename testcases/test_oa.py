from business.oa import OA
from business.usermanage import UserManage
from tools.timehandler import TimeHandler
# from config.parseconfig import data

class TestOA:

    def test_oa_checkin(self):
        um = UserManage('CP8vN2d3_6tp9COW_XZ0x2xjL5gzh9oRKSp-l2fgtcg')
        d1 = um.get_department()
        # print(d1.json())
        id = d1.json()['department'][0]['id']
        # print(id)
        u2 = um.get_user(id)
        # print(u2.json())
        user_list = [u2.json()['userlist'][0]['userid']]


        oa = OA('gPo9q2e_9qmsDxcGnrPfCxWjRcaiE3nv2XTFzFrneKs')

        date1 = TimeHandler().current_time()
        date2 = TimeHandler().string_toTimestamp('2020-10-27 11:11:11')
        data = oa.get_checkin_data(opencheckindatatype=3,starttime=date2,endtime=date1,useridlist=user_list)
        print(data.json())