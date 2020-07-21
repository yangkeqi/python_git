import requests,json

class API(object):
    def get_method(self,url,data=None,headers=None):
        if headers is not None:
            res = requests.get(url,params=data,header=headers)
            return json.loads(res.text)
        else:
            res = requests.get(url,params=data)
            return json.loads(res.text)

    def post_method(self,url,data=None,headers=None):
        if headers is not None:
            res = requests.post(url, data=json.dumps(data), headers=headers)
            return json.loads(res.text)
        else:
            res = requests.post(url, data=json.dumps(data))
            return res

    def run_method(self,method,url,data=None,headers=None):
        if method == 'get' or method == 'GET':
            res = self.get_method(url,data)
            return json.loads(res.text)
        elif method == 'post' or method == 'POST':
            res = self.post_method(url,data,headers)
            return json.loads(res.text)
        else:
            print('请求方式错误！！！！')

