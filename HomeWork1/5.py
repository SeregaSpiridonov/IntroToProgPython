#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

from cmath import sqrt

def PointDistance():
    xa = int(input('Точка А, x= '))
    ya = int(input('Точка А, y= '))
    xb = int(input('Точка B, x= '))
    yb = int(input('Точка B, y= '))
    dist = sqrt((xb - xa)**2 + (yb - ya)**2)
    print(round(dist.real, 3))
PointDistance()