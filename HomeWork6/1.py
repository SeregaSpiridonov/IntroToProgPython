# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
# приоритет операций стандартный.
        
def Calc(str1):
    string = str1.split()
    for i in range(len(string)):
        if string[i].isdigit():
            string[i] = int(string[i])
    pr1 = {'*': lambda x, y: x * y,
            '/': lambda x, y: x / y,}
    pr2 = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,}
    j = 0
    while ('*' in string) or ('/' in string):
        if string[j] in pr1:
            temp = pr1[string[j]](string[j - 1], string[j + 1])
            del string[j - 1 : j + 2]
            string.insert(j - 1, temp)
            j = 0
        else:
            j += 1
    j = 0
    while ('+' in string) or ('-' in string):
        if string[j] in pr2:
            temp = pr2[string[j]](string[j - 1], string[j + 1])
            del string[j - 1 : j + 2]
            string.insert(j - 1, temp)
            j = 0
        else:
            j += 1 
    print(*string)
Calc('1 - 2 * 3')



# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

def UniqSearch(List1):
    someDict = {}
    someList = []
    for i in List1:
        if i not in someDict:
            someDict[i] = 1
        else:
            someDict[i] += 1
    for key, val in someDict.items():
        if val == 1:
            someList.append(key)
    return someList

print(UniqSearch([1, 2, 3, 5, 1, 5, 3, 10]))