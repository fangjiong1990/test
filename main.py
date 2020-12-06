from time import strftime, localtime
import datetime

def print_hi(name):

    print('Hi', {name})
    print(datetime.datetime.now())
    print(strftime('%Y-%m-%d %H:%M:%S', localtime()))

    for i in range(1,10):
        for j in range(1, i+1):
            print(j, "*", i, "=", i*j, end=" ")
        print()


if __name__ == '__main__':
    print_hi('PyCharm')
