# Сиденко Анастасия, ИУ7-23Б комбинированный метод(хорд и касательных)

# gran,vvod,step,iter,toch - границы, шаг, количество итераций, точность
# table - таблица
# a,b,h,kolj,eps - границы, шаг, количество итераций, точность
# extremum - экстремумы функции
# s,x,y - массивы переменыых и их значений
# m - меню
# root,naz - главное окно, название

import matplotlib.pyplot as plt
import numpy as np
from math import *
from tkinter import *

root = Tk()

naz = Label(text='Приближенное решение алгебралического уравнения \n\
            sin(x) = 0 \n\
            комбинированным методом',font='arial 14')

naz.grid(column=1,row=1,columnspan=6)

# функция
def func(x):
    return x*x-4

# 1 производная
def func1(x):
    
    return 2*x

# 2 производная
def func2(x):
    return 2

# границы
gran = Label(text='Введите границы ')
grana = Label(text='a = ')
vvoda = Entry(width=10)
granb = Label(text='b = ')
vvodb = Entry(width=10)

gran.grid(column=1,row=2)
grana.grid(column=2,row=2)
vvoda.grid(column=3,row=2)
granb.grid(column=4,row=2)
vvodb.grid(column=5,row=2)

# шаг
step = Label(text='Введите шаг')
steph = Entry(width=10)

step.grid(column=1,row=3)
steph.grid(column=2,row=3)

# число итераций
itera = Label(text='Введите максимальное \nчисло итераций ')
iterai = Entry(width=10)

itera.grid(column=1,row=4)
iterai.grid(column=2,row=4)

# точность
toch = Label(text='Введите точность\nвычислений')
toche = Entry(width=10)

toch.grid(column=1,row=5)
toche.grid(column=2,row=5)

# шапка таблицы
table1s = Label(root,relief=SUNKEN,text='Номер',width=20,height=3)
table2s = Label(root,relief=SUNKEN,text='Интервал',width=20,height=3)
table3s = Label(root,relief=SUNKEN,text='Значение\nприближенного\nкорня',
               width=20,height=3)
table4s = Label(root,relief=SUNKEN,text='Значение фунции\nот приближенного\nкорня',
               width=20,height=3)
table5s = Label(root,relief=SUNKEN,text='Количество\nитераций',width=20,height=3)
table6s = Label(root,relief=SUNKEN,text='Код ошибки',width=20,height=3)
table1s.grid(row=7,column=1)
table2s.grid(row=7,column=2)
table3s.grid(row=7,column=3)
table4s.grid(row=7,column=4)
table5s.grid(row=7,column=5)
table6s.grid(row=7,column=6)


# обновление значений в таблице
def obnov():
    # чтение значений и проверка на корректность

    a=0
    b=0
    h=0
    eps=0
    kolj=0
    f = False
    otvx =[]
    otvy =[]
    try:
        a = float(vvoda.get())
        b = float(vvodb.get())
        h = float(steph.get())
        eps = float(toche.get())
        kolj = int(iterai.get())
        f = True
    except:
        window = messagebox.showinfo('Информация','Проверьте ввод')

    # если все ОК со вводом
    if f:
        s = np.arange(a,b+h,h)

        for j in range(15):
            pust=Label(width=125)
            pust.grid(column=1,row=8+j,columnspan=6)

        # комбинированный метод
        def komb(a,b):
            j = 0
            while abs(b-a) > 2*eps:
                if func1(a)*func2(a)>0:
                    a = a - (func(a)*(b-a)/(func(b)-func(a)))
                    b = b - func(b)/func1(b)
                    j+=1
                else:
                    b = b - (func(b)*(b-a)/(func(b)-func(a)))
                    a = a - func(a)/func1(a)
                    j+=1

            if j<=kolj:
                return (b+a)/2,j
            else:
                return False,False
        n=0
        
        # добавление значений в таблицу
        for i in range(len(s)-1):

            if func(s[i])*func(s[i+1])<0:
                x,j = komb(s[i],s[i+1])
                n+=1
                table1 = Label(root,relief=SUNKEN,text=n,width=20)
                table2 = Label(root,relief=SUNKEN,
                               text='['+str(s[i])+','+str(s[i+1])+']',width=20)
                table1.grid(row=7+n,column=1)
                table2.grid(row=7+n,column=2)
                if x:
                    if x>s[i] and x<s[i+1]:
                        table3 = Label(root,relief=SUNKEN,
                                       text=round(x,5),width=20)
                        table4 = Label(root,relief=SUNKEN,
                                       text='{0:1.2e}'.format(func(x)),width=20)
                        table5 = Label(root,relief=SUNKEN,text=j,width=20)
                        table6 = Label(root,relief=SUNKEN,
                                       text='Нет ошибки',width=20)
                        table3.grid(row=7+n,column=3)
                        table4.grid(row=7+n,column=4)
                        table5.grid(row=7+n,column=5)
                        table6.grid(row=7+n,column=6)
                        otvx.append(x)
                        otvy.append(0)
                    else:
                        table3 = Label(root,relief=SUNKEN,text='-',width=20)
                        table4 = Label(root,relief=SUNKEN,text='-',width=20)
                        table5 = Label(root,relief=SUNKEN,text='-',width=20)
                        table6 = Label(root,relief=SUNKEN,text='2',width=20)
                        table3.grid(row=7+n,column=3)
                        table4.grid(row=7+n,column=4)
                        table5.grid(row=7+n,column=5)
                        table6.grid(row=7+n,column=6)
                else:
                    table3 = Label(root,relief=SUNKEN,text='-',width=20)
                    table4 = Label(root,relief=SUNKEN,text='-',width=20)
                    table5 = Label(root,relief=SUNKEN,text='-',width=20)
                    table6 = Label(root,relief=SUNKEN,text='1',width=20)
                    table3.grid(row=7+n,column=3)
                    table4.grid(row=7+n,column=4)
                    table5.grid(row=7+n,column=5)
                    table6.grid(row=7+n,column=6)
                    
            if func(s[i])==0:
                n+=1
                table1 = Label(root,relief=SUNKEN,text=n,width=20)
                table2 = Label(root,relief=SUNKEN,
                               text='['+str(s[i])+','+str(s[i+1])+']',width=20)
                table3 = Label(root,relief=SUNKEN,text=s[i],width=20)
                table4 = Label(root,relief=SUNKEN,text=func(s[i]),width=20)
                table5 = Label(root,relief=SUNKEN,text=1,width=20)
                table6 = Label(root,relief=SUNKEN,text='Нет ошибки',width=20)
                table1.grid(row=7+n,column=1)
                table2.grid(row=7+n,column=2)
                table3.grid(row=7+n,column=3)
                table4.grid(row=7+n,column=4)
                table5.grid(row=7+n,column=5)
                table6.grid(row=7+n,column=6)
                otvx.append(s[i])
                otvy.append(0)
        if func(s[-1])==0:
                n+=1
                table1 = Label(root,relief=SUNKEN,text=n,width=20)
                table2 = Label(root,relief=SUNKEN,
                               text='['+str(s[-2])+','+str(s[-1])+']',width=20)
                table3 = Label(root,relief=SUNKEN,text=s[-1],width=20)
                table4 = Label(root,relief=SUNKEN,text=func(s[-1]),width=20)
                table5 = Label(root,relief=SUNKEN,text=1,width=20)
                table6 = Label(root,relief=SUNKEN,text='Нет ошибки',width=20)
                table1.grid(row=7+n,column=1)
                table2.grid(row=7+n,column=2)
                table3.grid(row=7+n,column=3)
                table4.grid(row=7+n,column=4)
                table5.grid(row=7+n,column=5)
                table6.grid(row=7+n,column=6)
                otvx.append(s[-1])
                otvy.append(0)
        # нахождение экстремумов
        x = np.arange(a,b,0.001)
        extremumx=[]
        extremumy=[]
        for i in range(len(x)):
            if round(func1(x[i]),3)==0.0:
                extremumx.append(x[i])
                extremumy.append(func(x[i]))

        # построение графика
        y = np.sin(x)
        plt.plot(x,y)
        plt.grid(True)
        plt.scatter(extremumx, extremumy, s=60, c='red')
        plt.xlabel('Yellow - solution, red - extremum')
        plt.scatter(otvx, otvy, s=60, c='yellow')
        plt.show()

# кнопка обновления 
ok = Button(text='Обновить значения',command=obnov)
ok.grid(column=2,row=6,columnspan=2)

# меню ошибок
def osh1():
    window = messagebox.showinfo('Информация',
                                 'Превышено допустимое число итераций')
def osh2():
    window = messagebox.showinfo('Информация','Выход за границы функции')

m = Menu(root)
root.config(menu=m)
sm = Menu(m)
m.add_cascade(label='Ошибки',menu=sm)
sm.add_command(label='1',command=osh1)
sm.add_command(label='2',command=osh2)

root.mainloop()



