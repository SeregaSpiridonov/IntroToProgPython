# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

from random import randint


def DeleteABC():
    data = open ('w1r.txt', 'r', encoding='utf-8')
    myStr = data.read()
    data.close()
    someList = myStr.split(' ')
    filterStr = ' '.join((filter(lambda s: 'абв' not in s, someList)))
    data = open ('w1wr.txt', 'w', encoding='utf-8')
    data.write(filterStr)
    data.close()


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому 
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

def GameCand():
    Player1 = input('Введите имя первого игрока: ')
    Player2 = input('Введите имя второго игрока(для игры с ботом введите "bot"): ')
    cand = 2021
    flag = randint(1, 2)
    print(f'Начинает игрок: {flag}.')
    if Player2 == 'bot':
        while cand > 0:
            p1Cand = 0
            p2Cand = 0
            if flag == 1:
                p1Cand = int(input(f'Игрок {Player1} берёт конфет: '))
                while p1Cand > 28 or p1Cand < 1 or p1Cand > cand:
                    print(f'Введено некоректное кол-во конфет, введите от 1-28 и не больше чем {cand}.')
                    p1Cand = int(input(f'Игрок {Player1} берёт конфет: '))
                cand -= p1Cand
                flag = 2
                print(f'Конфет осталось: {cand}.')
            elif flag == 2:
                if cand <= 28:
                    p2Cand = cand
                else:
                    p2Cand = randint(1, 28)
                print(f'Игрок {Player2} берёт конфет: {p2Cand}')
                cand -= p2Cand
                flag = 1
                print(f'Конфет осталось: {cand}.')
        if flag == 1:
            print(f'Победил {Player2}')
        else: print(f'Победил {Player1}')
        exit()
    else:
        while cand > 0:
            p1Cand = 0
            p2Cand = 0
            if flag == 1:
                p1Cand = int(input(f'Игрок {Player1} берёт конфет: '))
                while p1Cand > 28 or p1Cand < 1 or p1Cand > cand:
                    print(f'Введено некоректное кол-во конфет, введите от 1-28 и не больше чем {cand}.')
                    p1Cand = int(input(f'Игрок {Player1} берёт конфет: '))
                cand -= p1Cand
                flag = 2
                print(f'Конфет осталось: {cand}.')
            elif flag == 2:
                p2Cand = int(input(f'Игрок {Player2} берёт конфет: '))
                while p2Cand > 28 or p2Cand < 1 or p2Cand > cand:
                    print(f'Введено некоректное кол-во конфет, введите от 1-28 и не больше чем {cand}.')
                    p2Cand = int(input(f'Игрок {Player2} берёт конфет: '))
                cand -= p2Cand
                flag = 1
                print(f'Конфет осталось: {cand}.')
        if flag == 1:
            print(f'Победил {Player2}')
        else: print(f'Победил {Player1}')


#Создайте программу для игры в ""Крестики-нолики"".

def PrintTab(list1):
    print(f'|{list1[0]}|{list1[1]}|{list1[2]}|')
    print(f'|{list1[3]}|{list1[4]}|{list1[5]}|')
    print(f'|{list1[6]}|{list1[7]}|{list1[8]}|')
def FindXorO(x, list1):
    if list1[x] == 'X' or list1[x] == 'O': return True
    else: return False
def FindWin(list1):
    myList = ['X', 'O']
    for w in myList:
        if list1[0] == w and list1[1] == w and list1[2] == w: return True
        elif list1[3] == w and list1[4] == w and list1[5] == w: return True
        elif list1[6] == w and list1[7] == w and list1[8] == w: return True
        elif list1[0] == w and list1[4] == w and list1[8] == w: return True
        elif list1[2] == w and list1[4] == w and list1[6] == w: return True
        elif list1[0] == w and list1[3] == w and list1[6] == w: return True
        elif list1[1] == w and list1[4] == w and list1[7] == w: return True
        elif list1[2] == w and list1[5] == w and list1[8] == w: return True
    return False     
def GameXorO():
    Player1 = input('Введите имя первого игрока: ')
    Player2 = input('Введите имя второго игрока: ')
    cand = 2021
    flag = randint(1, 2)
    if flag == 1: print(f'Начинает {Player1} - X.')
    else: print(f'Начинает {Player2} - O.')
    gameList = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    PrintTab(gameList)
    while flag != 3:
        if flag == 1:
            p1 = (int(input(f'{Player1}: Введите номер поля от 1 - 9: '))) - 1
            while p1 < 0 or p1 > 8 or FindXorO(p1, gameList) == True:
                print('Ошибка на этом месте уже стоит Х или О, либор число >9 или <1')
                p1 = (int(input(f'{Player1}: Введите номер поля от 1 - 9: '))) - 1
            gameList[p1] = 'X'
            flag = 2
            PrintTab(gameList)
            if FindWin(gameList) == True:
                print(f'Выйграл {Player1}!')
                exit()
        elif flag == 2:
            p2 = (int(input(f'{Player2}: Введите номер поля от 1 - 9: '))) - 1
            while p2 < 0 or p2 > 8 or FindXorO(p2, gameList) == True:
                print('Ошибка на этом месте уже стоит Х или О, либор число >9 или <1')
                p2 = (int(input(f'{Player2}: Введите номер поля от 1 - 9: '))) - 1
            gameList[p2] = 'O'
            flag = 1
            PrintTab(gameList)
            if FindWin(gameList) == True:
                print(f'Выйграл {Player2}!')
                exit()


def EncodeMess():
    data = open('w4re.txt', 'r')
    text = data.read()
    data.close()
    encodedString = ""
    i = 0
    while (i <= len(text)-1):
        count = 1
        temp = text[i]
        j = i
        while (j < len(text)-1):  
            if (text[j] == text[j + 1]): 
                count += 1
                j += 1
            else: break
        encodedString = encodedString + str(count) + temp
        i = j + 1
    data = open('w4wr.txt', 'w')
    data.write(encodedString)
    data.close()

def decodeMess():
    data = open('w4wr.txt', 'r')
    text = data.read()
    data.close()
    decodedString = ""
    i = 0
    j = 0
    while (i <= len(text) - 1):
        count = int(text[i])
        temp = text[i + 1]
        for j in range(count):
            decodedString = decodedString + temp
        i += 2
    data = open('w4re.txt', 'w')
    data.write(decodedString)
    data.close()

#DeleteABC()
#GameCand()
#GameXorO()
#EncodeMess()
decodeMess()