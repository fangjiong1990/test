from time import strftime, localtime
import datetime

def print_hi(name):

    print('Hi', {name})
    print(datetime.datetime.now())
    print(strftime('%Y-%m-%d %H:%M:%S', localtime()))


if __name__ == '__main__':
    print_hi('PyCharm')
