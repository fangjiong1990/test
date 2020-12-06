from DemoAPI.lib.readConfig import readConfig

class geturlParams:
    def get_url(self):
        new_url = readConfig().get_http('scheme') + '://' + readConfig().get_http('baseurl') + ':8888' + '/login'
        return new_url

if __name__ == '__main__':
    print(geturlParams().get_url())