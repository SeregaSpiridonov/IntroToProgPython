from log import loger
def data_add():
    f = open('data.txt', 'a', encoding="utf-8")
    user_list = input('Введите данные через пробел: ')
    f.writelines(f'\n{user_list}')
    loger(user_list, 3)
    f.close()
