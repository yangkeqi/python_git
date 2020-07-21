import requests,json
from common.mylog import Log_Maker
class API:
    def api_method(self,method,url,parma=None,header=None):
        global res
        session = requests.session()
        if method == ('get' or 'GET'):
            if header is None:
                try:
                    res = session.request(method=method,url=url,params=parma)
                    return res.json()
                except:
                    return res
            else:
                try:
                    head = {'Content-type': 'application/x-www-form-urlencoded'}
                    res = session.request(method=method,url=url,params=parma,headers=head)
                    return res.json()
                except:
                    return res
        elif method == ('post' or 'POST'):
            if header is None:
                try:
                    res = session.request(method=method,url=url,data=json.loads(parma))
                    return res.json()
                except Exception as result:
                    Log_Maker('ERROR', result)
                    return result
            else:
                try:
                    res = session.request(method=method,url=url,data=json.loads(parma),headers=header)
                    return res.json()
                except:
                    return res
        else:
            print('请求方法错误！！')