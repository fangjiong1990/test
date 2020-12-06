import configparser
from DemoAPI.config.setting import TEST_CONFIG

config = configparser.ConfigParser()
config.read(TEST_CONFIG, encoding='utf-8')

class readConfig:
    def get_http(self, name):
        value = config.get('http', name)
        return value

if __name__ == '__main__':
    print(readConfig().get_http('baseurl'))
    print(readConfig().get_http('port'))