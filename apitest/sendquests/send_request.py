import requests


class MaoYan:
    def send_request(self, params, baseurl):
        url = "https://maoyan.com{}".format(baseurl)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47",
        }
        response = requests.get(url=url, params=params, headers=headers)
        return response


if __name__ == '__main__':
    print(MaoYan().send_request().text)
