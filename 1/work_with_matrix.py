# матрица

# ИУ7-13Б Сиденко Анастасия

# m - размер матрицы
# a - матрица
# i, j - счетчики
# otr - кол-во отрицательных
# otrm - минимальное количество отрицательных
# iminotr - столбец с минимальным кол-вом отрицательных
# b - элементы находящиеся над побочой диагональю

m = 0
while m == 0:
    try:
        m = int(input('Введите размер матрицы '))
    except:
        print('Некорректное значение, введите еще раз')
    if m <= 0:
        print('Некорректное значение, введите еще раз')
        m = 0
        
a = [[0]*m for i in range(m)]
kol=0
print('Введите матрицу ')
for i in range(m):
    j = 0
    while j<m:
        try:
            a[i][j] = float(input())
        except:
            j-=1
            print('Некорректное значение, введите еще раз')
        j+=1

print('Исходная матрица ')         
for i in range(m):
    for j in range(m):
        print(' {:6.2f}'.format(a[i][j]), end=' ')
    print('\n')

otr = 0
otrm = m+1
iminotr = 0
for j in range(m):
    otr = 0
    for i in range(m):
        if a[i][j] < 0:
            otr+=1
    if (otr < otrm) and (otr > 0):
        otrm = otr
        iminotr = j+1
if otrm == m+1:
    print('Отрицательных элементов нет\n')
else:
    print('Минимальное количество отрицательных в ',iminotr,' столбце \n')
    
b = []
for i in range(m-1,-1,-1):
    for j in range(m-i-1):
        b.append(a[i][j])
print('Элементы находящиеся над побочной диагональю ')
print(b)
