# Сиденко Анастасия, ИУ7-23Б

# root - окно
# lab - заголовок
# text1,text2 - поля для воода
# but1,but0,but2 - кнопки алфавита сс
# butu - кнпоки удаления
# a,b,c - тексты
# otv - результат
# butv, buts - кнпоки суммы и разности
# child,osh - окно ошибки
# name,nm - окно автора
# m,sm - выпадающее меню
# a10,b10,c10,k,zpa,zpb,z1,z2,m - вспомогательные переменные

from tkinter import *
from math import *
root = Tk()

# Название
lab = Label(root, text='Сложение и вычитание \nв троично-симметричной\n системе счисления', font='Arial 12')
lab.grid(row=0,column=0,columnspan=8)

# Ввод
text1 = Text(width=20,height=2)
text1.grid(row=1,column=0, columnspan=4, rowspan = 2)

text2 = Text(width=20,height=2)
text2.grid(row=1,column=5, columnspan=4, rowspan = 2)

# Кнопки1
def output1(event):
    text1.insert(END,'+')
    otv['text']='Результат: '
but1 = Button(root,text='+')
but1.bind('<Button-1>',output1)
but1.grid(row=3,column=0)
def output0(event):
    text1.insert(END,'0')
    otv['text']='Результат: '
but0 = Button(root,text='0')
but0.bind('<Button-1>',output0)
but0.grid(row=3,column=1)
def output2(event):
    text1.insert(END,'-')
    otv['text']='Результат: '
but2 = Button(root,text='-')
but2.bind('<Button-1>',output2)
but2.grid(row=3,column=2)



# Кнопки2
def output1(event):
    text2.insert(END,'+')
    otv['text']='Результат: '
but1 = Button(root,text='+')
but1.bind('<Button-1>',output1)
but1.grid(row=3,column=5)
def output0(event):
    text2.insert(END,'0')
    otv['text']='Результат: '
but0 = Button(root,text='0')
but0.bind('<Button-1>',output0)
but0.grid(row=3,column=6)
def output2(event):
    text2.insert(END,'-')
    otv['text']='Результат: '
but2 = Button(root,text='-')
but2.bind('<Button-1>',output2)
but2.grid(row=3,column=7)


# Кнопки удаления
def udal1(event):
    text1.delete('1.0',END)
    otv['text']='Результат: '
butu = Button(root,text='очистить 1 поле')
butu.bind('<Button-1>',udal1)
butu.grid(row=4,column=0,columnspan=4)
def udal2(event):
    text2.delete('1.0',END)
    otv['text']='Результат: '
butu = Button(root,text='очистить 2 поле')
butu.bind('<Button-1>',udal2)
butu.grid(row=4,column=5,columnspan=4)
def udal3(event):
    text1.delete('1.0',END)
    text2.delete('1.0',END)
    otv['text']='Результат: '
butu = Button(root,text='очистить оба поля')
butu.bind('<Button-1>',udal3)
butu.grid(row=5,column=4)

# Проверка

def keypress(event):
    otv['text']='Результат: '
    a = text1.get('1.0',END)
    b = text2.get('1.0',END)
    # проверка на корректный ввод и удаление
    if len(a)>1:
        for i in range(len(a)-1):
            if (a[i] not in '+-0'):
                text1.delete('1.0',END)
                text1.insert(END,a[:i])
                text1.insert(END,a[i+1:len(a)-1])
    if len(b)>1:
        for i in range(len(b)-1):
            if (b[i] not in '+-0'):
                text2.delete('1.0',END)
                text2.insert(END,b[:i])
                text2.insert(END,b[i+1:len(b)-1])
root.bind('<Any-KeyRelease>',keypress)

# Результат
otv = Label(root, text='Результат:')
otv.grid(row=6,column=0,columnspan=8)

# Кнопки суммы
def visum():
    a = text1.get('1.0',END)
    a = a[:len(a)-1]
    b = text2.get('1.0',END)
    b = b[:len(b)-1]
    # перевод чисел в 10
    if len(a)>0 and len(b)>0:
        a10=0
        b10=0
        for i in range(len(a)-1,-1,-1):
            if a[i]=='+':
                a10+=3**(len(a)-1-i)
            if a[i]=='-':
                a10-=3**(len(a)-1-i)
  
        for i in range(len(b)-1,-1,-1):
            if b[i]=='+':
                b10+=3**(len(b)-1-i)
            if b[i]=='-':
                b10-=3**(len(b)-1-i)

        c10 = a10+b10
        c=[]
        if c10<0:
            m=-1
        else:
            m=1
        # перевод обратно, проверка на отрицательное 
        c10=abs(c10)
        while c10>2:
            k=c10%3
            c10=c10//3
            if k==2:
                c.append('-')
                c10+=1
            if k==1:
                c.append('+')
            if k==0:
                c.append('0')
        if c10==2:
            c.append('-')
            c.append('+')
        if c10==1:
            c.append('+')
        if c10==0 and len(c)==0:
            c.append('0')
        if m<0:
            for i in range(len(c)):
                if c[i]=='+':
                    c[i]='-'
                elif c[i]=='-':
                    c[i]='+'
        c = list(reversed(c))
        otv['text']='Результат: '+''.join(c)
    else:
        child = Toplevel(root)
        child.title('Ошибка')
        osh = Label(child,text='Проверьте корректность ввода!', font='Arial 12')
        osh.grid()
def summ(event):
    visum()
buts = Button(root,text='сумма')
buts.bind('<Button-1>',summ)
buts.grid(row=1,column=4)

# Кнопки разности    
def vidiff():
    a = text1.get('1.0',END)
    a = a[:len(a)-1]
    b = text2.get('1.0',END)
    b = b[:len(b)-1]
    # перевод чисел в 10
    if len(a)>0 and len(b)>0:
        a10=0
        b10=0
        for i in range(len(a)-1,-1,-1):
            if a[i]=='+':
                a10+=3**(len(a)-1-i)
            if a[i]=='-':
                a10-=3**(len(a)-1-i)
  
        for i in range(len(b)-1,-1,-1):
            if b[i]=='+':
                b10-=3**(len(b)-1-i)
            if b[i]=='-':
                b10+=3**(len(b)-1-i)

        c10 = a10+b10
        c=[]
        if c10<0:
            m=-1
        else:
            m=1
        # перевод обратно, проверка на отрицательное
        c10=abs(c10)
        while c10>2:
            k=c10%3
            c10=c10//3
            if k==2:
                c.append('-')
                c10+=1
            if k==1:
                c.append('+')
            if k==0:
                c.append('0')
        if c10==2:
            c.append('-')
            c.append('+')
        if c10==1:
            c.append('+')
        if c10==0 and len(c)==0:
            c.append('0')
        if m<0:
            for i in range(len(c)):
                if c[i]=='+':
                    c[i]='-'
                elif c[i]=='-':
                    c[i]='+'
        c = list(reversed(c))
        otv['text']='Результат: '+''.join(c)
    else:
        child = Toplevel(root)
        child.title('Ошибка')
        osh = Label(child,text='Проверьте корректность ввода!', font='Arial 12')
        osh.grid()
def diff(event):
    vidiff()
butv = Button(root,text='разность')
butv.bind('<Button-1>',diff)
butv.grid(row=2,column=4)

# автор
def name():
    nam = Toplevel(root)
    nam.title('Автор')
    nm = Label(nam,text='Сиденко Анастасия\nИУ7-23Б', font='Arial 12')
    nm.grid()
    
# закрыть окно
def ex():
    root.destroy()
    
# меню
m = Menu(root)
root.config(menu=m)
sm = Menu(m)
m.add_cascade(label="Меню",menu=sm)
sm.add_command(label="Сумма",command=visum)
sm.add_command(label="Разность",command=vidiff)
sm.add_command(label="Сведения об авторе",command=name)
sm.add_command(label="Закрыть",command=ex)

root.mainloop()
