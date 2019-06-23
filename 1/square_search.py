# Массив

# Сиденко Анастасия. ИУ7-13Б

# m - массив
# kol - количесво элементов массива
# n - количество перемен знака
# x - вводимое значение
# f - проверка
# p - квадрат числа
# k - количество чисел являющихся квадратами

from math import sqrt

m = []
print('Введите массив ')
kol = 0
n = x = 0
x = input()
f = True
while x != 'exit':
    f = True
    if x!='':
        if x[0] == '-' or x[0].isdigit():
            i = 1
            while i<(len(x)):
                if x[i] == '.':
                    break
                if x[i].isdigit() == 0:
                    f = False
                i+=1
            i+=1
            for k in range(i,len(x)):
                if x[k].isdigit() == 0:
                    f = False
        else:
            f = False
        if f:
            m.append(float(x))
            kol+=1
        else:
            print('Некорректное значение введите еще раз ')
    else:
        print('Некорректное значение введите еще раз ')
    x = input()
    
print('Данный массив\n',m)

k = 0
s = 0
while s*s < m[0]:
    s+=1
if s*s == m[0]:
    k+=1
for i in range (1,kol):
    s = 0
    if (m[i]<0 and m[i-1]>=0) or (m[i]>=0 and m[i-1]<0):
        n+=1
    while s*s < m[i]:
        s+=1
    if s*s == m[i]:
        k+=1

print('Количество чисел, являющихся полными квадратами ',k)
print('Количество перемен знака ',n)
