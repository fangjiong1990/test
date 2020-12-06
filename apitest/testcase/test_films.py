import unittest, ddt
from sendquests.send_request import MaoYan
from readdata.readexcel import ReadExcel


testData = ReadExcel().read_data()

@ddt.ddt
class TestSelectFilms(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @ddt.data(*testData)
    def test_films(self,data):
        response = MaoYan().send_request(eval(data['params']), data['url'])
        if data['UserCase'] == '喜剧':
            self.assertEquals(response.status_code, 200)
            self.assertIn("喜剧", response.text)
        if data['UserCase'] == '爱情':
            self.assertEquals(response.status_code, 200)
            self.assertIn("爱情", response.text)
        if data['UserCase'] == '剧情':
            self.assertEquals(response.status_code, 200)
            self.assertIn("剧情", response.text)

