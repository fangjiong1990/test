import requests, json


class RunMain:

    # 定义一个方法，传入需要的参数url和data
    def send_post(self, url, data):
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        pass

    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        return result

if __name__ == '__main__':
    result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name':'xiaoming', 'pwd':'11'})
    print(result)