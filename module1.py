from math import*
try:
    a=float(input("a"))
    b=float(input("b"))
    c=float(input("c"))
    D = b ** 2 - 4 * a * c
    if D < 0:
        print('Корней нет')
    if D == 0:
        x1 = -b / (2 * a)
    if D >0:
        x1 = -b + sqrt(D) / (2 * a)
        x2 = -b - sqrt(D) / (2 * a)


except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    a=0
    print("a=0 вот тебе и ошибка")
except ZeroDivisionError:
    D=0
    print("Дискриминант равен нулю")




