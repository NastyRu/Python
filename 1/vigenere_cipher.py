# Шифр Виженера

# Сиденко, ИУ7-13

# vij - матрица
# i,j,m,n,k - счетчики
# kluch - ключ
# stk - данная строка
# got - результат


vij = [[0]*26 for i in range(26)]
m = 1
for i in range(26):
    for j in range(26):
        if (j+m) < 27:
            vij[i][j]=j+m
        else:
            vij[i][j]=j+m-26
    m+=1


print('Выберите, что надо сделать: ')
print('1) Зашифровать')
print('2) Расшифровать')
n = int(input())
kluch = input('Введите ключ ')
stk = input('Введите строку ')
got = []

    
if n == 1:
    for i in range(len(stk)):
        got.append(vij[ord(kluch[i%len(kluch)])-65][ord(stk[int(i)])-65])   
if n == 1:
    print('Зашифрованное слово ')
    for i in range(len(got)):
            print(chr(got[i]+64),end='')

k = 0
if n == 2:
    for i in range(len(stk)):
        for j in range(26):
            if vij[ord(kluch[i%len(kluch)])-65][j] == (ord(stk[int(i)])-64):
                k = j
                break
        got.append(k)
if n == 2:
    print('Расшифрованное слово ')
    for i in range(len(got)):
            print(chr(got[i]+65),end='')
