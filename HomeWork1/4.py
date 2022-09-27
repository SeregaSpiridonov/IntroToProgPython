#Напишите программу, которая по заданному номеру четверти, показывает 
#диапазон возможных координат точек в этой четверти (x и y).

def CoordinateRange():
    quarter = int(input('Введите номер четверти(1-4): '))
    if quarter == 1:
        print('x, y от 0 до ∞')
    elif quarter == 2:
        print('x от 0 до -∞, y от 0 до ∞')
    elif quarter == 3:
        print('x, y от 0 до -∞')
    elif quarter == 4:
        print('x от 0 до ∞, y от 0 до -∞')
    else: print('Нет такой четверти!')
CoordinateRange()