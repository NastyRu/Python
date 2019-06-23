# Численное интегрирование

# Сиденко Анастасия, ИУ7-13Б

# i1 - граница 1 для метода левых многоугольников
# i2 - граница 2 для метода левых многоугольников
# i3 - граница 1 для метода Симпсона
# i4 - граница 2 для метода Симпсона
# eps - точность
# n - количество итераций для достижения точности

import math

# проверка на вещественное число
def vesh(x):
    x = input()
    f = False
    while f == False:
        f = True
        if x!='':
            if ((x[0] == '-' or x[0] == '+') and len(x)>1) or x[0].isdigit():
                i = 1
                while i<(len(x)) and x[i]!='e':
                    if x[i] == '.':
                        i+=1
                        break
                    if x[i].isdigit() == 0:
                        f = False
                    i+=1
                while i<(len(x)) and x[i]!='e':
                    if x[i].isdigit() == 0:
                        f = False
                    i+=1
                if i<len(x):
                    if x[i]=='e':
                        if len(x)>(i+1):
                            if x[i+1]=='-' or x[i+1]=='+':
                                if len(x)>(i+2):
                                    for k in range(i+2,len(x)):
                                        if x[k].isdigit() == 0:
                                            f = False
                                else:
                                    f = False
                            elif x[i+1].isdigit():
                                for k in range(i+1,len(x)):
                                    if x[k].isdigit() == 0:
                                        f = False
                            else:
                                f = False
            else:
                f = False
            if f:
                x = float(x)
                f = True
            else:
                print('Некорректное значение введите еще раз ')
                x = input()
        else:
            print('Некорректное значение введите еще раз ')
            x = input()
    return x

# проверка на натуральное число
def nat(n):
    T = True
    while T:
        n = input()
        if n.isdigit():
            n = int(n)
            T = False
        else:
            print('Некорректный ввод, введите еще раз ')
        if n == 0:
            T = True
            print('Некорректный ввод, введите еще раз ')
    return n

print('Введите левую границу ')
a = 0
a = vesh(a)

print('Введите правую границу ')
b = 0
b = vesh(b)

print('Введите количество итераций n1 ')
n1 = 0
n1 = nat(n1)

      
print('Введите количество итераций n2 ')
n2 = 0
n2 = nat(n1)

# функция
def func(x):
    return x

# метод Симпсона
if b>a:
    def method1(n): 
        k = (b-a)/n
        x = a
        i = 0
        while x<b:
            i += k/6*(func(x)+4*func(x+k/2)+func(x+k))
            x+=k
        return i
else:
    def method1(n): 
        k = (a-b)/n
        x = b
        i = 0
        while x<a:
            i += k/6*(func(x)+4*func(x+k/2)+func(x+k))
            x+=k
        return -i

# левые прямоугольники
if b>a:
    def method2(n): 
        k = (b-a)/n
        x = a
        i = 0
        while x<=b:
            i += func(x)*k
            x+=k
        return i
else:
    def method2(n): 
        k = (a-b)/n
        x = b
        i = 0
        while x<a:
            i += func(x)*k
            x+=k
        return -i


i1 = method2(n1)
i2 = method2(n2)
i3 = method1(n1)
i4 = method1(n2)

print('┌───────────────┬─────────────────┬────────────────┐')
print('│               │       N1        │        N2      │')
print('├───────────────┼─────────────────┼────────────────┤')
print('│  Метод левых  │',' {: 12.7e} │ {: 12.7e} │'.format(i1,i2))
print('│прямоугольников│                 │                │')
print('├───────────────┼─────────────────┼────────────────┤')
print('│     Метод     │',' {: 12.7e} │ {: 12.7e} │'.format(i3,i4))
print('│    Симпсона   │                 │                │')
print('└───────────────┴─────────────────┴────────────────┘')

print('Введите точность ')
eps = 0
eps = vesh(eps)
t = True
if eps <= 0:
    while t:
        print('Некорректный ввод, введите еще раз ')
        eps = 0
        eps = vesh(eps)
        if eps>0:
            t = False
n = 2

if abs(i1-i2) > abs(i3-i4):
    print('Наименее точный метод левых прямоугольников')
    while abs(method1(n)-method1(2*n)) >= eps:
        n*=2
else:
    print('Наименее точный метод Симпсона')
    while abs(method2(n)-method2(2*n)) >= eps:
        n*=2
print('Количество итераций для достижения точности эпсилон',n)
        

