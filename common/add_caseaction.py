from common.Read_excel import excelaction
from common.conf import conf
#封装执行excel的方法，返回excel内的数据
class add_caseaction():
    @staticmethod
    def add_case():
        result = conf().get_config()
        excel_path = result['Environments']['test']['excelpath']
        sheet_name = excelaction.get_all_sheets(excel_path)
        test_suite = []
        if result['Run_all']['Whether'] == True:
            for i in range(len(sheet_name)):
                sh = sheet_name[i]
                # 获取每个sheet行数
                rows,sh1 = excelaction.openexcel(excel_path, sh)
                for j in range(rows-1):
                    #返回单挑测试用例数据
                    testData = excelaction.getexcelparams(excel_path, sh,j+1)
                    test_suite.append(testData)
            return test_suite
        elif result['Run_all']['Whether'] == False:
            for i in (result['Moudle']):
                sheetname = result['Moudle'][str(i)]['sheetname']
                beginrow = result['Moudle'][str(i)]['start']  # 起始执行ID
                # 如果起始ID为空，从第二行执行
                if beginrow == None:
                    beginrow = 2
                endrow = result['Moudle'][str(i)]['end']  # 结束ID
                for j in range(beginrow, endrow + 1):
                    testData = excelaction.getexcelparams(excel_path, sheetname, j-1)
                    test_suite.append(testData)
            return test_suite
        else:
            print('执行模式 Run_all Whether 配置错误只能为true/false')

