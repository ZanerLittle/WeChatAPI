import os,json

class ConfigHandler:

    def __init__(self):
        self.configpath = os.path.join(os.path.dirname(__file__))

    def parse_json(self,jsonname = 'config.json'):
        jsonpath = os.path.join(self.configpath,jsonname)
        data = json.load(open(jsonpath))
        return data
C1 = ConfigHandler()
data= C1.parse_json()


if __name__ == '__main__':
    print(ConfigHandler().parse_json())