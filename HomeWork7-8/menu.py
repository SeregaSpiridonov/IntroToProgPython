import os
import sys
from search_data import txt_input
from search_data import search
from search_data import print_all
from export import data_add


def print_menu():
    print('''Это пользовательский интерфейс
Вы можете: 1. Показать все данные
           2. Найти человека
           3. Записать данные 
           4. Выход из программы
             ''')


def input_option():
    number = '0'
    while number not in '1 2 3 4'.split():
        number = input('Введите число: ')
    return number


def interface():
    while True:
        os.system('cls')
        print_menu()
        number = input_option()
        if number == '1':
            os.system('cls')
            txt = txt_input('data.txt')
            print_all(txt)
        elif number == '2':
            os.system('cls')
            search()
        elif number == '3':
            data_add()
        elif number == '4':
            sys.exit()
