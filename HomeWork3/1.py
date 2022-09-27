# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def SumUneven(list1):
    sum = 0
    i = 1
    while i < len(list1):
        sum += list1[i]
        i += 2
    print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def MultiplicationCouple(list1):
    someList = []
    j = len(list1) - 1
    i = 0
    while i <= j:
        someList.append(list1[i] * list1[j])
        j -= 1
        i += 1
    print(someList)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def FractDifference(list1):
    someList = []
    dif = 0
    for i in list1:
        x = round(i - int(i), 3)
        if x > 0:
            someList.append(x)
    dif = round(max(someList) - min(someList), 3)
    print(dif)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def ConvertInBinary(number):
    someList =[]
    while number > 0:
        someList.insert(0, number %2)
        number = int(number / 2)
    print(''.join([str(i) for i in someList]))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonachi(num):
    if num >= 0:
        list1 = [0,1]
        for j in range(2, num + 1):
           list1.append(list1[j-1] + list1[j-2])
        return list1[num]
    else:
        num = -(num-1)
        list1 = [1,0]
        for j in range(2, num + 1):
            list1.append(list1[j-2] - list1[j-1]) 
        list1.reverse()
    return list1[0]
def Fibo(k):
    someList = []
    for i in range((-k), k+1):
        someList.append(Fibonachi(i))
    print(someList)

# SumUneven([2, 3, 5, 9, 3])
# MultiplicationCouple([2, 3, 4, 5, 6])
# FractDifference([1.1, 1.2, 3.1, 5, 10.01])
# ConvertInBinary(45)
Fibo(8)