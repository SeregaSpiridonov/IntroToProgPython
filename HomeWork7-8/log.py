import datetime


def loger(data, flag):
    if flag == 0: fg = 'Print data'
    if flag == 1: fg = 'Read_all'
    if flag == 2: fg = 'Search'
    if flag == 3: fg = 'Write'
    f = open('logData.txt', 'a', encoding="utf-8")
    num = f.writelines(f'\n{fg} - {data} - {datetime.datetime.now().ctime()}')
    f.close()