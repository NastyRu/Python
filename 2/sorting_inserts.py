# Сиденко Анастасия, ИУ7-23Б

# Сортировкка вставками

# root - главное окно
# inizsort,vvodrazm,vvodgran,mas -массив проверки работы сортировки
# tic,toc - таймер
# array,v - массив
# n,a,b - количество элементов, границы
# widow - окно ошибки
# table - таблица
# inizmas,vvodsort,vvodgran,vvodrazm - массив для замера времени


from tkinter import *
from random import *
from time import time

# главное окно
root = Tk()
root.title('Сортировка вставками')

# параметры для проверки работы монтировки
inizsort = Label(root,text = 'Проверка корректности работы на массиве малой размерности',font='arial 14')
vvodrazm = Label(root,text = 'Введите размерность: ',font='arial 10')
vvodrazmentrym = Entry(root)
vvodgranm = Label(root,text = 'Введите границы:   от',font='arial 10')
vvodlevm = Entry(root)
vvodgrandom = Label(root,text = 'до')
vvodpravm = Entry(root)

mas = Label(root,text = 'Неотсортированный массив: '+'Отсортированный массив: ',font='arial 12')


# сортировка вставками
def sortvs(array):
    tic = time()
    for i in range(len(array)):
        v = array[i]
        j=i
        while (int(array[j-1])>int(v)) and (j>0):
            array[j]=array[j-1]
            j-=1
        array[j]=v
    toc = time()
    return tic,toc
    
# сортировка проверочного массива
def arm():
    array=[]
    if vvodrazmentrym.get().isdigit() and vvodlevm.get().isdigit() and vvodpravm.get().isdigit():
        n=int(vvodrazmentrym.get())
        a=int(vvodlevm.get())
        b=int(vvodpravm.get())
        for i in range(n):
            array.append(str(randint(a,b)))
        mas['text']= 'Неотсортированный массив: '+';'.join(array)
        sortvs(array)
        mas['text']+='  Отсортированный массив: '+';'.join(array)
    else:
        window = messagebox.showinfo('Информация','Проверьте ввод')

# вывод массива
ok1 = Button(root,text='OK',command=arm)

# создание таблицы
table11 = Label(root,relief=SUNKEN,width=20,font='arial 10')
table12 = Label(root,relief=SUNKEN,text='N1',width=40,font='arial 10')
table13 = Label(root,relief=SUNKEN,text='N2',width=40,font='arial 10')
table14 = Label(root,relief=SUNKEN,text='N3',width=40,font='arial 10')
table21 = Label(root,relief=SUNKEN,text='↑',width=20,font='arial 10')
table22 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table23 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table24 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table31 = Label(root,relief=SUNKEN,text='rand',width=20,font='arial 10')
table32 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table33 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table34 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table41 = Label(root,relief=SUNKEN,text='↓',width=20,font='arial 10')
table42 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table43 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')
table44 = Label(root,relief=SUNKEN,text='time',width=40,font='arial 10')

# сортировка и засечение времени сортировки
def arb():
    if vvodrazmentry1.get().isdigit() and vvodrazmentry2.get().isdigit() and vvodrazmentry3.get().isdigit() and\
       vvodlevb.get().isdigit() and vvodpravb.get().isdigit():
        n1 = int(vvodrazmentry1.get())
        n2 = int(vvodrazmentry2.get())
        n3 = int(vvodrazmentry3.get())
        a = int(vvodlevb.get())
        b = int(vvodpravb.get())
        array=[]
        for i in range(n1):
            array.append(str(randint(a,b)))
        arraypr=sorted(array)
        tic,toc=sortvs(arraypr)
        table22['text']=round(toc-tic,6)
        arrayobr=arraypr[::-1]
        tic,toc=sortvs(arraypr)
        table42['text']=round(toc-tic,6)
        tic,toc=sortvs(array)
        table32['text']=round(toc-tic,6)

        array=[]
        for i in range(n2):
            array.append(str(randint(a,b)))
        arraypr=sorted(array)
        tic,toc=sortvs(arraypr)
        table23['text']=round(toc-tic,6)
        arrayobr=arraypr[::-1]
        tic,toc=sortvs(arraypr)
        table43['text']=round(toc-tic,6)
        tic,toc=sortvs(array)
        table33['text']=round(toc-tic,6)
        
        array=[]
        for i in range(n3):
            array.append(str(randint(a,b)))
        arraypr=sorted(array)
        tic,toc=sortvs(arraypr)
        table24['text']=round(toc-tic,6)
        arrayobr=arraypr[::-1]
        tic,toc=sortvs(arraypr)
        table44['text']=round(toc-tic,6)
        tic,toc=sortvs(array)
        table34['text']=round(toc-tic,6)
    else:
        window = messagebox.showinfo('Информация','Проверьте ввод')

# параметры сортировки 3 массивов
inizmas = Label(root,text = 'Подсчет времени сортировки на трех различных масивах',font='arial 14')
vvodrazmb = Label(root,text = 'Введите 3  размерности: ',font='arial 10')
vvodrazmentry1 = Entry(root)
vvodrazmb1 = Label(root,text = 'N1 = ',font='arial 10')
vvodrazmentry2 = Entry(root)
vvodrazmb2 = Label(root,text = 'N2 = ',font='arial 10')
vvodrazmentry3 = Entry(root)
vvodrazmb3 = Label(root,text = 'N3 = ',font='arial 10')
vvodgranb = Label(root,text = 'Введите границы:   от',font='arial 10')
vvodlevb = Entry(root)
vvodgrandob = Label(root,text = 'до',font='arial 10')
vvodpravb = Entry(root)
ok2 = Button(root,text='OK',command=arb)

# 1 строка, проверка работы
inizsort.grid(row=1,column=1,columnspan=7)

# 2 строка, ввод размерности
vvodrazm.grid(row=2,column=1)
vvodrazmentrym.grid(row=2,column=2)

# 3 строка, границы сортировки
vvodgranm.grid(row=3,column=1)
vvodlevm.grid(row=3,column=2)
vvodgrandom.grid(row=3,column=3)
vvodpravm.grid(row=3,column=4)

# 4 строка, кнопка ОК
ok1.grid(row=4,column=4)

# 5 строка, вывод массивов
mas.grid(row=5,column=1,columnspan=7)

# 6 строка, подсчет времени
inizmas.grid(row=6,column=1,columnspan=7)

# 7 строка, ввод размерности
vvodrazmb.grid(row=7,column=1)
vvodrazmb1.grid(row=7,column=2)
vvodrazmentry1.grid(row=7,column=3)
vvodrazmb2.grid(row=7,column=4)
vvodrazmentry2.grid(row=7,column=5)
vvodrazmb3.grid(row=7,column=6)
vvodrazmentry3.grid(row=7,column=7)

# 8 строка, воод границ
vvodgranb.grid(row=8,column=1)
vvodlevb.grid(row=8,column=2)
vvodgrandob.grid(row=8,column=3)
vvodpravb.grid(row=8,column=4)

# 9 строка, кнопка ОК
ok2.grid(row=9,column=4)

# 10,11,12,13 строки - таблица
table11.grid(row=10,column=1)
table12.grid(row=10,column=2,columnspan=2)
table13.grid(row=10,column=4,columnspan=2)
table14.grid(row=10,column=6,columnspan=2)
table21.grid(row=11,column=1)
table22.grid(row=11,column=2,columnspan=2)
table23.grid(row=11,column=4,columnspan=2)
table24.grid(row=11,column=6,columnspan=2)
table31.grid(row=12,column=1)
table32.grid(row=12,column=2,columnspan=2)
table33.grid(row=12,column=4,columnspan=2)
table34.grid(row=12,column=6,columnspan=2)
table41.grid(row=13,column=1)
table42.grid(row=13,column=2,columnspan=2)
table43.grid(row=13,column=4,columnspan=2)
table44.grid(row=13,column=6,columnspan=2)

root.mainloop()
