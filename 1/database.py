# База данных
# Сиденко Анастасия, ИУ7-13Б

import pickle
import os

bd = [{'фильм':'Чарли и шоколадная фабрика','год':'2005','жанр':'Фэнтези','длительность':'115'},
      {'фильм':'Турист','год':'2010','жанр':'Боевик','длительность':'103'},
      {'фильм':'Пираты Карибского моря','год':'2003','жанр':'Фэнтези','длительность':'143'},
      {'фильм':'Алиса в стране чудес','год':'2010','жанр':'Приключения','длительность':'108'},
      {'фильм':'Суини Тодд, демон-парикмахер с Флит-стрит','год':'2007','жанр':'Ужасы','длительность':'116'},
      {'фильм':'Сонная лощина','год':'1999','жанр':'Ужасы','длительность':'105'},
      {'фильм':'Убийство в Восточном экспрессе','год':'2017','жанр':'Драма','длительность':'114'},
      {'фильм':'Превосходство','год':'2014','жанр':'Триллер','длительность':'119'},
      {'фильм':'Эдвард руки-ножницы','год':'1990','жанр':'Фэнтези','длительность':'105'},
      {'фильм':'Волшебная страна','год':'2004','жанр':'Драма','длительность':'97'}]

sim = '\|/:*?"<>+%!@ '

# разбиение строки
def split(stroka):
    razd = ' ,-/'
    sim = []
    k = 0
    elem = ''
    for i in range(len(stroka)):
        if stroka[i] in razd:
            for j in range(k,i):
                elem+=stroka[j]
            k = i+1
            if elem:
                sim.append(elem)
            elem=''
    for j in range(k,len(stroka)):
            elem+=stroka[j]
    if elem:
        sim.append(elem)
    return sim

numbers = {1:'фильм', 2:'год', 3:'жанр', 4:'длительность'}
l = list(numbers.keys())
l.sort()

# поиск элементов, удовлетворяющих параметрам
def poisk():
    film = input('Название фильма ')
    god = input('Введите год или промежуток лет, через пробел ')
    ganr = input('Введите жанр или несколько через пробел ')
    dlit = input('Введите длительность в минутах или промежуток через пробел ')
    god = split(god)
    ganr = split(ganr)
    dlit = split(dlit)
    podhod=[0]*len(bd)
    if film:
        for i in range(len(bd)):
            if bd[i]['фильм'].lower()==film.lower():
                podhod[i]+=1
    else:
        for i in range(len(bd)):
            podhod[i]+=1
    if god:
        if len(god)==1:
            for i in range(len(bd)):
                if bd[i]['год']==god[0]:
                    podhod[i]+=1
        else:
            for i in range(len(bd)):
                if god[0]<=bd[i]['год']<=god[1]:
                    podhod[i]+=1
    else:
        for i in range(len(bd)):
            podhod[i]+=1
    if ganr:
        for i in range(len(bd)):
            if bd[i]['жанр'].lower() in ganr:
                podhod[i]+=1
    else:
        for i in range(len(bd)):
            podhod[i]+=1
    if dlit:
        if len(dlit)==1:
            for i in range(len(bd)):
                if bd[i]['длительность']==dlit[0]:
                    podhod[i]+=1
        else:
            for i in range(len(bd)):
                if dlit[0]<=bd[i]['длительность']<=dlit[1]:
                    podhod[i]+=1
    else:
        for i in range(len(bd)):
            podhod[i]+=1
    return podhod

# меню
def menu():
    print('Выберите, что надо сделать ')
    print('1. Создать новую базу данных')
    print('2. Открыть базу данных')
    print('3. Просмотр всех элементов базы данных')
    print('4. Добавление элементов в базу данных')
    print('5. Поиск элементов в базе данных')
    print('6. Удаление элементов из базы данных')
    print('0. Выйти')

menu()
k = input()

T = True
while T:
    dur = 1
    # создание новой БД
    if k == '1':
        naz = input('Введите имя, без расширения ')
        F = True
        while F:
            F = False
            for i in range(len(naz)):
                if naz[i] in sim:
                    F = True
            if F:
                naz = input('Некорректное имя файла, введите еще раз ')
        f = open(naz,'wb')
        pickle.dump(bd,f)
        f.close()
        print('База данных создана ')
        print()
    # открытие БД
    elif k == '2':
        naz = input('Введите имя ')
        if os.path.exists(naz):
            f = open(naz,'rb')
            print('База данных открыта')
            f.close()
        else:
            print('Такого файла не существует')
        print()
    # вывод БД
    elif k == '3':
        for i in range(1,5):
            print(numbers[i].upper(),end=' '*(42-len(numbers[i])))
        print()
        for i in range(len(bd)):
            for j in l:
                print(bd[i][numbers[j]],end=' '*(42-len(bd[i][numbers[j]])))
            print()
        print()
    # добавление новых данных
    elif k == '4':
        film = input('Введите название фильма ')
        F = True
        while F:
            if film:
                F = False
            else:
                film = input('Некорректный ввод, введите еще раз ')
        god = input('Введите год ')
        F = True
        while F:
            if god.isdigit():
                F = False
            else:
                god = input('Некорректный ввод, введите еще раз ')
        janr = input('Введите жанр ')
        F = True
        while F:
            if janr.isalpha():
                F = False
            else:
                janr = input('Некорректный ввод, введите еще раз ')
        dlit = input('Введите длительность в минутах ')
        F = True
        while F:
            if dlit.isdigit():
                F = False
            else:
                dlit = input('Некорректный ввод, введите еще раз ')
        bd.append({'фильм':film,'год':god,'жанр':janr.lower(),'длительность':dlit})
        print('Элемент добавлен')
        print()
    # поиск по базе данных
    elif k == '5':
        print('Введите критерии по которым будем искать, если\n',
              'какой-то критерий не нужен, оставьте поле не заполненным ')
        podhod = poisk()
        c=0
        for i in range(len(bd)):
            if podhod[i] == 4:
                for j in l:
                    print(bd[i][numbers[j]],end=' '*(42-len(bd[i][numbers[j]])))
                    с+=1
                print()
        if c==0:
            print('Таких элементов не найдено')
        print()
    # удаление из базы данных
    elif k == '6':
        print('Введите критерии по которым будем удалять, если\n',
              'какой-то критерий не нужен, оставьте поле не заполненным ')
        podhod = poisk()
        udal=[]
        for i in range(len(bd)):
            if podhod[i] == 4:
                udal.append(i)
        с = 0
        if len(udal)>0:
            for i in range(len(udal)):
                bd.pop(udal[i]-с)
                с+=1
            print('Полученная база данных ')
            for i in range(len(bd)):
                for j in l:
                    print(bd[i][numbers[j]],end=' '*(42-len(bd[i][numbers[j]])))
                print()
        else:
            print('Таких элементов не найдено')
        print()
    elif k == '0':
        T = False
    else:
        dur = 0
        print('Некорректный ввод, введите еще раз')
    if T:
        if dur:
            menu()
        k = input()
        
    
