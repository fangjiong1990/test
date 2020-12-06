from DemoAPI.lib.configHttp import RunMain
from DemoAPI.lib.geturlParams import geturlParams
from DemoAPI.lib.readexcel import ReadExcel
import unittest

class testUserLogin(unittest.TestCase):

    def description(self):
        self.case_name

    def setUp(self) -> None:
        print('測試開始前準備')

    def tearDown(self) -> None:
        print('測試結束，輸出log完結')

    def test01case(self):
        self.checkResult()

    def checkResult(self):
        method = ReadExcel().read_data()[0]['method']
        url = geturlParams().get_url()
        params = eval(ReadExcel().read_data()[0]['params'])
        UserCase = ReadExcel().read_data()[0]['UserCase']
        info = RunMain().run_main(method, url, params)
        res = eval(info)
        if UserCase == '登錄成功':
            self.assertEqual(res['code'], 200)
        else:
            print("測試錯誤")