import yaml

class conf:
    def get_config(self):
        f = open('E:/Test_Auto/config.yaml',encoding='utf-8')
        res = yaml.load(f,Loader=yaml.FullLoader)
        return res

