import time
from log import loger


def txt_input(file_name):
    f = open(file_name, 'r', encoding="utf-8")
    num = f.readlines()
    user_list = []
    for i in num:
        raw_test = i.split()
        user_data = {'LastName': raw_test[0],
                     'Name': raw_test[1], 'Number': raw_test[2]}
        user_list.append(user_data)
    f.close()
    return user_list


def search():
    list = txt_input('data.txt')
    request = input('Кого искать?: ').lower()
    loger(request, 2)
    switch = True
    for data in list:
        if data['LastName'].lower() == request or data['Name'].lower() == request or data['Number'] == request:
            print(*data.values())
            loger(data, 0)
            switch = False
    if switch == True:
        print('Нет совпадений.')
    input('Нажмите Enter для продолжения')


def print_all(list):
    loger('data', 1)
    for i in list:
        print(i)
        time.sleep(0.2)
    input('Введите Enter')
