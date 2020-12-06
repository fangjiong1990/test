import unittest
from mail.my_yagmail import send_mail
from time import strftime
from htmltestrunner.HTMLTestRunner import HTMLTestRunner

class RunTestCase:
    def add_case(self):
        """加载所有的测试用例"""
        # case地址
        test_path = "testcase\\"

        #报告地址
        report_url = "report\\"

        # 获取当前时间
        nowtime = strftime("%Y_%m_%d_%H_%M_%S")

        filename =  report_url +nowtime + "_result.html"
        fp = open(filename, "wb")
        discover = unittest.defaultTestLoader.discover(test_path, pattern="test_*.py")
        # runner = unittest.TextTestRunner()
        runner = HTMLTestRunner(stream=fp,
                       title='接口自动化测试报告',
                       description='环境：windows 10 浏览器：chrome',
                       tester='FangJiong')
        runner.run(discover)
        fp.close()
        send_mail(filename)
        print("发送完成")

if __name__ == '__main__':
    RunTestCase().add_case()