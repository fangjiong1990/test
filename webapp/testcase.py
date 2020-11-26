from selenium import webdriver

class Baidu:
    def test_baidu(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        self.driver.quit()


if __name__ == '__main__':
    baidu = Baidu()
    baidu.test_baidu()