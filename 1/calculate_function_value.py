# Вычисление значений функции,вариант 4

# Сиденко Анастасия, ИУ7-13Б

# a, b, x - вводимые данные
# c - котангенс
# f - значение функции
# i - счетчик
# g - повторяющаяся функция
# m - проверка

from math import tan, sin, pi, e

for i in range(2):

    a, b, x = map(float,input('Введите данные ').split())

    c = 1/tan(a*b)
    m = True

    if c > 0:
        f = c - e*e
    else:
        g = 0.93*pi*pi*sin(x)
        if g > 0:
            f = g**(-0.2)
        elif g == 0:
            print('Делить на 0 нельзя')
            m = False 
        else:
            f = -1*abs(g)**(-0.2)

    if m:
        print('Функция = ','{:7.3f}'.format(f))
