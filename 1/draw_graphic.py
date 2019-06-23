# Вычисление значений функций и построение графика

# Сиденко Анастасия, ИУ7-13Б

# z - переменная
# s1, s2 - функции
# p1, p2 - количество положительных элемeнтов
# n, k - начальное значение и конечное значение Х
# h - шаг
# kol - количество точек
# m - номер точки
# s1min, s2min - максимальное и минимальное значение функции
# mn - номер минимального
# xo - длина отрицательной части
# p - размер пробела на графике
# q - размер 10 позиций
# i, j - счетчики

from math import exp

z = [0]*100000
s1 = [0]*100000
s2 = [0]*100000
m = [0]*100000
n = float(input('Начальное значение Z '))
k = float(input('Конечное значение Z '))
h = float(input('Шаг '))
z[0] = n
p1 = p2 = kol = 0
s1min = s1max = s1pmin = 20.1
mn = 0


# чертим шапку таблицы
print('┌────────────────────────────────┐')
print('│ z           s1            s2   │')
print('├────────────────────────────────┤')


# вычисляем значение функций, находим мин и макс, кол-во положительных
# чертим таблицу
while z[kol] <= (k + h/2):
    s1[kol] = z[kol]**3 - 4.51*z[kol]**2 - 23.9*z[kol] + 20.1
    s2[kol] = exp(-z[kol]) - (z[kol]-1)**2
    if s1[kol] > s1max:
        s1max = s1[kol]
    if s1[kol] < s1min:
        s1min = s1[kol]
    if (s1[kol] < s1pmin) and (s1[kol] > 0):
        s1pmin = s1[kol]
        mn = kol
    if s1[kol] > 0:
        p1+=1
    if s2[kol] > 0:
        p2+=1
    if z[kol] >= 0:
        print('│ {:2.2f}''{:13.3f}''{:13.3f} │'.format(z[kol],s1[kol],s2[kol]))
    else:
        print('│{:2.2f}''{:13.3f}''{:13.3f} │'.format(z[kol],s1[kol],s2[kol]))
    kol+=1
    z[kol] = z[kol-1]+h
print('└────────────────────────────────┘')   
print('\nКоличество положительных 1 функции ',p1)
print('\nКоличество положительных 2 функции ',p2)
print('\n')


# вычисляем номера позиций
for i in range(kol):
    m[i] = round(60*(s1[i]-s1min)/(s1max-s1min))
    if (s1[i]  == s1pmin):
        mn = i
xo = m[mn]

p = (s1max-s1min)/(max(m)+3)*16
print('       ',end='')
# строим график
q = s1min  
print(' {:10.2f}     '.format(q),end='')
for j in range(0,max(m),15):
    q+=p
    print('{:10.2f}     '.format(q),end='')
print()
if z[0]<0:
    print('{:10.2f}   '.format(z[0]),end='')
else:
    print('{:10.2f}   '.format(z[0]),end='')
for j in range(max(m)+3):
    if j == m[0]:
        print('*',end='')
    elif j == xo-1:
        print('┬',end='')
    elif j%15 == 0:
        print('┴',end='')
    else:
        print('─',end='')
print('⟶ y')
for j in range(1,kol):
    if z[j]<0:
        print('{:10.2f}  '.format(z[j]),end='')
    else:
        print('{:10.2f}  '.format(z[j]),end='')
    if xo < m[j]:
        for i in range(xo):
            print(' ',end='')
        print('│',end='')
        for i in range(m[j]-xo):
            print(' ',end='')
        print('*')
    elif xo == m[j]:
        for i in range(xo):
            print(' ',end='')
        print('*')
    else:
        for i in range(m[j]):
            print(' ',end='')
        print('*',end='')
        for i in range(xo-m[j]-1):
            print(' ',end='')
        print('│')
for i in range(xo+12):
    print(' ',end='')
print('↓ z',end='')



