# Определение:
# длин сторон треугольника,
# длины медианы, проведенной из наименьшего угла
# равнобедренности
# принадлежности точки плоскости треугольника
# и максимальное расстояние от нее до стороны, если принадлежит

# Сиденко Анастасия, ИУ7-13Б

# х1, у1 - координаты первой точки
# х2, у2 - координаты второй точки
# х3, у3 - координаты третьей точки
# х, у - координаты точки
# a, b, c - стороны треугольника
# m - медиана
# s - минимальная сторона треугольника
# sa, sb, sc - площади маленьких треугольников
# so - суммарная площадь маленьких треугольников
# st - площадь данного треугольника
# ha, hb, hc - высоты маленьких треугольников(расстояние от точки до стороны)
# h - максимальное расстояние от точки до стороны
# x12, x23, x13, y12, y23, y13 - повторяющиеся элементы

from math import sqrt

# ввод координат точек
x1, y1 = map(float, input('Введите координаты 1 точки ').split())
x2, y2 = map(float, input('Введите координаты 2 точки ').split())
x3, y3 = map(float, input('Введите координаты 3 точки ').split())

x12 = x1-x2
x23 = x2-x3
x13 = x1-x3
y12 = y1-y2
y23 = y2-y3
y13 = y1-y3

# вычисление длин сторон
a = sqrt(x12**2 + y12**2)
b = sqrt(x23**2 + y23**2)
c = sqrt(x13**2 + y13**2)

# все точки совпадают
if a == b == c == 0:
    print('Kоординаты всех точек совпадают') 
    
# совпадают 2 точки
elif (a == 0) or (a == 0) or (b == 0):
    print('Kоординаты двух точек совпадают')

# точки лежат на одной прямой
elif (a + b == c) or (c + b == a) or (a + c == b):
    print('Все точки лежат на одной прямой')

else:
    print('Стороны треугольника: ','{:7.3f}{:7.3f}{:7.3f}'.format(a,b,c))

    # напротив меньшей стороны лежит меньший угол, находим его
    s = min(a,b,c) 

    # вычисление длины медианы из наименьшего угла
    if s == a:
        #a
        m = sqrt(((x1+x2)/2-x3)**2 + ((y1+y2)/2-y3)**2)
    elif s == b:
        #b
        m = sqrt(((x3+x2)/2-x1)**2 + ((y3+y2)/2-y1)**2)
    else:
        #c
        m = sqrt(((x1+x3)/2-x2)**2 + ((y1+y3)/2-y2)**2)

    print('\nМедиана треугольника из наименьшего угла: ','{:7.3f}'.format(m))

    # проверка треугольника на равнобедренность
    if a == b or a == c or b == c:
        print('\nТреугольник равнобедренный')
    else:
        print('\nТреугольник неравнобедренный')
    
    # ввод координат точки и проверка на принадлежность плоскости треугольника
    x, y = map(float, input('\nВведите координаты точки ').split())

    # находим площади треугольников, образующихся данной точкой
    # и 2 точками треугольника и складываем полученные площади
    # находим площадь всего треугольника
    sa = 1/2*abs(x12*(y-y2)-(x-x2)*y12)
    sb = 1/2*abs(x23*(y-y3)-(x-x3)*y23)
    sc = 1/2*abs(-x13*(y-y1)+(x-x1)*y13)
    st = 1/2*abs(x13*y23-x23*y13)
    so = sa+sb+sc

    # проверяем равенство полученной суммарной площади и площади треугольника
    # если площади равны, значит точка принадлежит плоскости треугольника
    # если точка принадлежит, вычисляем расстояние от нее до сторон
    # через полученные площади маленьких треугольников
    if (so == st):
        print('Точка принадлежит плоскости треугольника')
        ha = 2*sa/a
        hb = 2*sb/b
        hc = 2*sc/c
        h = max(ha, hb, hc)
        print('Максимальное расстояние от точки до стороны ', '{:7.3f}'.format(h))
    else:
        print('Точка не принадлежит плоскости треугольника')
           
    
