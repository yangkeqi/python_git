from common.add_caseaction import add_caseaction
from common.conf import conf
from common.Read_excel import excelaction
from common.mylog import Log_Maker
from common.Api_Requests import API
from common.new_res import API
from ddt import ddt,data,unpack
import unittest,requests

test_data = add_caseaction.add_case()   #获取ddt需要执行的测试用例数据

@ddt
class excute_case(unittest.TestCase):
    @data(*test_data)
    def test_case(self,data):
        res_meth = data['请求方法']
        res_url = data['请求地址']
        res_par = data['请求参数']
        res = API().api_method(res_meth,res_url,res_par)



if __name__ == '__main__':
    unittest.main()