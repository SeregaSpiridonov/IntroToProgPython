#Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def ValidationAssertion():
    x = int(input('Введите Х= '))
    y = int(input('Введите Y= '))
    z = int(input('Введите Z= '))
    check1 = not (x or y or z)
    check2 = (not x) and (not y) and (not z)
    print(check1 == check2)
ValidationAssertion()