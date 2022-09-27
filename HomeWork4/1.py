# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.   10^{-1} ≤ d ≤10^{-10}

import math
from random import randrange

def AccuracyNumber():
    d = input('d: ')
    d1 = d.split('.')[1]
    num = float(input('Число: '))
    num1 = str(num).split('.')[0]
    resultNum = round(num, (len(d1)+1))
    resultNum = str(resultNum)[:(len(num1)+len(d1)+1)]
    while len(resultNum) < (len(d1) + len(num1) + 1):
        resultNum = resultNum + '0'
    print(resultNum)


# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

def ListMult(number):
    someList = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if(number % i == 0):
            count = 0
            while (number % i == 0):
                number //= i
                count += 1
            someList.append((i, count))
    if (number != 1): someList.append((number, 1))
    print('*'.join(['%d^%d' % i for i in someList]))


# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

def UniqueNumbers():
    someList = []
    sizeList = int(input('Введите количество чисел: '))
    for i in range(sizeList):
        someList.append(input(f'Введите число {i+1}: '))
    uNum = set(someList)
    print(uNum)


# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def ListRatio():
    k = int(input('k= '))
    someList = []
    k2 = k*k
    someList.append(k)
    if k > 1:
        while k2 <= 100:
            someList.append(k2)
            k2 *= k
    posit = randrange(0, len(someList))
    data = open('file.txt', 'w')
    data.writelines(f'{someList[posit]}*x^2 + 5 = 0')
    data.close()


#AccuracyNumber()
#ListMult(int(input('Введите натуральное число N: ')))
#UniqueNumbers()
ListRatio()