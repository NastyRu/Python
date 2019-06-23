# Определение параметров треугольной призмы

# Сиденко Анастасия, ИУ7-13Б

# r-радиус
# h-высота
# st-площадь треугольника
# v-объем призмы
# s-площадь боковой поверхности
# a-повторяющеея значение

import math as m
r,h=map(int,input('Введите радиус и высоту через пробел ').split())
a=3*m.sqrt(3)*r
st=a*r/4
v=st*h
s=a*h
print('Объем ', '{:7.3f}'.format(v))
print('Площадь треугольника ', '{:7.3f}'.format(st))
print('Площадь боковой поверхности ', '{:7.3f}'.format(s))