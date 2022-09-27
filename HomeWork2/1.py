# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import random

def SumNumbers():
    string1 = input('Введите число: ')
    string1 = string1.replace(',','0')
    string1 = string1.replace('.','0')
    length = len(string1)
    sum = 0
    for i in range(length):
        sum += int(string1[i])
    print(f'Сумма цифрв числе:',sum)


# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def CompositionNumbers():
    number = int(input('Введите N = '))
    numberList = []
    for i in range(1, number + 1):
        j = i - 1
        sum = 1
        while j > 0:
            composition = sum * j
            sum += composition
            j -= 1
        numberList.append(sum)
    print(numberList)

# Задайте список из n чисел последовательности (1 + (1/n))^n
# и выведите на экран их сумму.

def SequenceN():
    number = int(input('Введите N = '))
    listN = []
    for i in range(1 , number + 1):
        seq = (1 + (1 / i)) ** i
        listN.append(seq)
    print(f'Сумма чисел списка:', round(sum(listN), 2))

#Реализуйте алгоритм перемешивания списка.

def MixList():
    list1 = [5, 10, 0, -1, 100, -25]
    random.shuffle(list1)
    print(list1)

def ListNComposition(n):
    list1 = []
    composition = 1
    for i in range(n):
        a = random.randint(-n, n)
        list1.append(a)
    print(list1)
    with open ('file.txt', 'r') as data:
        for line in data:
            composition *= list1[int(line)]
    print(f'Произведение чисел на указанных позитиях в file.txt:\n',composition)

#SumNumbers()
#CompositionNumbers()
#SequenceN()
#MixList()
ListNComposition(10)